import os

import listaction
import countaction
import listallaction
import getaction

class GenericAction:
    def __init__(self, connection, table, destination_root) -> None:
        self.connection = connection
        self.table = table
        self.destination_root = destination_root
        cursor = connection.cursor()
        cursor.execute("SHOW COLUMNS FROM " + table)
        self.fields = cursor.fetchall()
        self.templateName = "GenericAction.tpl"
        self.listAction = listaction.ListAction(table,destination_root)
        self.listAllAction = listallaction.ListAllAction(table,destination_root)
        self.countAction = countaction.CountAction(table,destination_root)
        self.getAction = getaction.GetAction(table, self.fields, destination_root)

    def generate(self):

        # Create repository directory starting from the project root.
        path = os.path.join(self.destination_root,"src", "Application", "Actions", self.table.capitalize())
        print("Path di destinazione: ", path)
        if not os.path.exists(path):
            os.makedirs(path)

        # Generate repository file
        outputText = ""
        tplFile = os.path.join("templates",self.templateName)
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line \
                    .replace("##TABLENAMECAP##",self.table.capitalize(),-1) \
                    .replace("##TABLENAME##",self.table,-1)
        outputPath = os.path.join(path, self.table.capitalize()) + "Action.php"
        with open(outputPath,"w") as f:
            f.write(outputText)

        self.listAction.generate()
        self.countAction.generate()
        self.listAllAction.generate()
        self.getAction.generate()

