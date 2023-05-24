import os

class ListAllAction:
    def __init__(self, table, destination_root) -> None:
        self.table = table
        self.destination_root = destination_root
        self.templateName = "ListAllAction.tpl"

    def generate(self):

        # Create repository directory starting from the project root.
        path = os.path.join(self.destination_root,"src", "Application", "Actions", self.table.capitalize())
        print("Path di destinazione: ", path)

        # Generate repository file
        outputText = ""
        tplFile = os.path.join("templates",self.templateName)
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line \
                    .replace("##TABLENAMECAP##",self.table.capitalize(),-1) \
                    .replace("##TABLENAME##",self.table,-1)
        outputPath = os.path.join(path, self.table.capitalize()) + "ListAllAction.php"
        with open(outputPath,"w") as f:
            f.write(outputText)
