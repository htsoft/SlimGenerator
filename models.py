import os

import getter
import property
class Models:
    def __init__(self, table, fields, destination_root) -> None:
        self.table = table
        self.fields = fields
        self.destination_root = destination_root

    def Generate(self):
        # Crea la cartella del model nella posizione corretta della root del progetto.
        path = os.path.join(self.destination_root,"src", "Domain",self.table.capitalize())
        print("Path di destinazione: " , path)
        if not os.path.exists(path):
            os.makedirs(path)
        
        # Procede quindi alla creazione di tutti i files relativi al model nella cartella specificata
        properties = ""
        constructorParameters = ""
        constructorAssignments = ""
        getters = ""
        jsonfields = ""
        for (fname,type,nullable,key,defaultValue,extra) in self.fields:
            properties = properties + property.Property(fname,type,extra).generate()
            getters = getters + getter.Getter(fname,type,extra).generate()

            if "auto_increment" in extra:
                constructorParameters = constructorParameters + "?int $" + fname + ", "
            else:
                if "char" in type:
                    constructorParameters = constructorParameters + "string $" + fname + ", "
                elif "int" in type:
                    constructorParameters = constructorParameters + "int $" + fname + ", "
                elif "date" in type:
                    constructorParameters = constructorParameters + "string $" + fname + ", "
                elif "time" in type:
                    constructorParameters = constructorParameters + "string $" + fname + ", "
            constructorAssignments = constructorAssignments + "$this->" + fname + " = $" + fname + ";\r\t\t"
            jsonfields = jsonfields + "'" + fname + "' => $this->" + fname + ",\r\t\t\t"  
        constructorParameters = constructorParameters[:-2]

        # Genera il file del model
        outputText = ""
        tplFile = os.path.join("templates","Domain.tpl")
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line.replace("##TABLENAME##",self.table.capitalize(),-1).replace("##PROPERTIES##",properties,-1).replace("##CONSTRUCTORPARAMETERS##",constructorParameters,-1).replace("##CONSTRUCTORASSIGNMENTS##",constructorAssignments,-1).replace("##GETTERS##",getters,-1).replace("##JSONFIELDS##",jsonfields,-1)
        outputPath = os.path.join(path,self.table.capitalize()) + ".php"
        with open(outputPath,"w") as f:
            f.write(outputText)


        # Prepara la lista dei campi chiave
        keyFields = ""
        for (fname,type,nullable,key,defaultValue,extra) in self.fields:
            if "PRI" in key:
                if "char" in type:
                    keyFields = keyFields + "string $" + fname + ", "
                elif "int" in type:
                    keyFields = keyFields + "int $" + fname + ", "
                elif "date" in type:
                    keyFields = keyFields + "string $" + fname + ", "
                elif "time" in type:
                    keyFields = keyFields + "string $" + fname + ", "
        keyFields = keyFields[:-2]

        # Gestione del file di interfaccia per il repository
        outputText = ""
        tplFile = os.path.join("templates","DomainRepositoryInterface.tpl")
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line.replace("##TABLENAME##",self.table.capitalize(),-1).replace("##KEYFIELDS##",keyFields,-1)
        outputPath = os.path.join(path,self.table.capitalize()) + "Repository.php"
        with open(outputPath,"w") as f:
            f.write(outputText)

        # Gestione del file dell'eccezione
        outputText = ""
        tplFile = os.path.join("templates","DomainException.tpl")
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line.replace("##TABLENAME##",self.table.capitalize(),-1)
        outputPath = os.path.join(path,self.table.capitalize()) + "NotFoundException.php"
        with open(outputPath,"w") as f:
            f.write(outputText)
