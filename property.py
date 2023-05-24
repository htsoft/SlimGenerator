import os

class Property:
    def __init__(self, fname, type, extra) -> None:
        self.fname = fname
        self.type = type
        self.extra = extra
        self.getterFileName = "ModelProperty.tpl"

    def generate(self):
        outputText = ""

        tplFile = os.path.join("templates",self.getterFileName)
        type = ""

        if "auto_increment" in self.extra:
            type = "?int"
        else:
            if "int" in type:
                type = "int"
            elif "float" in type:
                type = "float"
            elif "double" in type:
                type = "double"
            else:
                type = "string"
        with open(tplFile,"r") as f:
            lines = f.readlines()
            for line in lines:
                outputText = outputText + line.replace("##FIELDNAME##",self.fname,-1).replace("##TYPE##",type,-1)

        return outputText

