import os

class Repository:
    def __init__(self, connection, table, destination_root) -> None:
        self.connection = connection
        self.table = table
        self.destination_root = destination_root
        cursor = connection.cursor()
        cursor.execute("SHOW COLUMNS FROM " + table)
        self.fields = cursor.fetchall()
        self.templateName = "DBRepository.tpl"

    def generate(self):
        # USE clauses
        useClauses = 'use App\\Domain\\' + self.table.capitalize() + '\\' + self.table.capitalize() + ';\r'
        useClauses = useClauses + 'use App\\Domain\\' + self.table.capitalize() + '\\' + self.table.capitalize() + 'NotFoundException;\r'
        useClauses = useClauses + 'use App\\Domain\\' + self.table.capitalize() + '\\' + self.table.capitalize() + 'Repository;\r'

        # Create repository directory starting from the project root.
        path = os.path.join(self.destination_root,"src", "Infrastructure", "Persistence", self.table.capitalize())
        print("Path di destinazione: " , path)
        if not os.path.exists(path):
            os.makedirs(path)

        # Fields list
        fieldsList = ""
        fieldsRows = ""
        fieldsParams = ""
        fieldsInsertArray = ""
        whereKey = ""
        whereArray = ""
        updateFields = ""
        updateParams = ""
        keyFields = ""
        keyUpdateParams = ""
        keyParams = ""
        getArray = ""
        for (fname,type,nullable,key,defaultValue,extra) in self.fields:
            fieldsList = fieldsList + fname + ","
            fieldsRows = fieldsRows + "$row[\"" + fname + "\"],"
            fieldsParams = fieldsParams + ":" + fname + ","
            fieldsInsertArray = fieldsInsertArray + "\":" + fname + "\" => $data->get" + fname.capitalize() + "(),"
            if "PRI" in key:
                whereKey = whereKey + fname + "=:" + fname + " AND "
                whereArray = whereArray + "\":" + fname + "\" => $data->get" + fname.capitalize() + "(),"
                keyFields = keyFields + fname + ","
                keyUpdateParams = keyUpdateParams + "$data->get" + fname.capitalize() + "(),"
                getArray = getArray + "\":" + fname + "\" => $" + fname + ","
                if "int" in type:
                    keyParams = keyParams + "int $" + fname + ","
                elif "float" in type:
                    keyParams = keyParams + "float $" + fname + ","
                elif "double" in type:
                    keyParams = keyParams + "double $" + fname + ","
                else:
                    keyParams = keyParams + "string $" + fname + ","

            else:
                updateFields = updateFields + fname + "=:" + fname + ","
                updateParams = updateParams + "\":" + fname + "\" => $data->get" + fname.capitalize() + "(),"

        fieldsList = fieldsList[:-1]
        fieldsRows = fieldsRows[:-1]
        fieldsParams = fieldsParams[:-1]
        fieldsInsertArray = fieldsInsertArray[:-1]
        whereKey = whereKey[:-5]
        whereArray = whereArray[:-1]
        getArray = getArray[:-1]
        updateFields = updateFields[:-1]
        updateParams = updateParams + whereArray
        keyFields = keyFields[:-1]
        keyUpdateParams = keyUpdateParams[:-1]
        keyParams = keyParams[:-1]

        # Generate repository file
        outputText = ""
        tplFile = os.path.join("templates",self.templateName)
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line \
                    .replace("##TABLENAMECAP##",self.table.capitalize(),-1) \
                    .replace("##TABLENAME##",self.table,-1) \
                    .replace("##USECLAUSES##",useClauses,-1) \
                    .replace("##FIELDSLIST##",fieldsList,-1) \
                    .replace("##FIELDSROW##",fieldsRows,-1) \
                    .replace("##FIELDSPARAMS##",fieldsParams,-1) \
                    .replace("##FIELDSINSERTARRAY##",fieldsInsertArray,-1) \
                    .replace("##WHEREKEY##",whereKey,-1) \
                    .replace("##WHEREARRAY##",whereArray,-1) \
                    .replace("##GETARRAY##",getArray,-1) \
                    .replace("##UPDATEFIELDS##",updateFields,-1) \
                    .replace("##UPDATEARRAY##",updateParams,-1) \
                    .replace("##KEYFIELDS##",keyFields,-1) \
                    .replace("##KEYUPDATEPARAMS##",keyUpdateParams,-1) \
                    .replace("##KEYPARAMS##",keyParams,-1) 
        outputPath = os.path.join(path,"DB" + self.table.capitalize()) + ".php"
        with open(outputPath,"w") as f:
            f.write(outputText)

