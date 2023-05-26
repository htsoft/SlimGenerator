import os

class InsertAction:
    def __init__(self, table, fields, destination_root) -> None:
        self.table = table
        self.destination_root = destination_root
        self.fields = fields
        self.templateName = "InsertAction.tpl"

    def generate(self):

        # Create repository directory starting from the project root.
        path = os.path.join(self.destination_root,"src", "Application", "Actions", self.table.capitalize())
        print("Path di destinazione: ", path)

        # Cycle into the fields to generate all the necessary strings
        fields = ""
        for (fname,type,nullable,key,defaultValue,extra) in self.fields:
            fieldType = "";
            if "int" in type:
                fieldType = "(int)"
            elif "float" in type:
                fieldType = "(float)"
            elif "double" in type:
                fieldType = "(double)"
            
            fields = fields + fieldType + "$data->" + fname + ", ";
        fields = fields[:-2]

        # Generate repository file
        outputText = ""
        tplFile = os.path.join("templates",self.templateName)
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line \
                    .replace("##TABLENAMECAP##",self.table.capitalize(),-1) \
                    .replace("##TABLENAME##",self.table,-1) \
                    .replace("##FIELDS##",fields,-1) 
        outputPath = os.path.join(path, self.table.capitalize()) + "InsertAction.php"
        with open(outputPath,"w") as f:
            f.write(outputText)
