import models

class Entita:
    def __init__(self, connection, table, destination_root) -> None:
        self.connection = connection
        self.table = table
        self.destination_root = destination_root
        cursor = connection.cursor()
        cursor.execute("SHOW COLUMNS FROM " + table)
        self.fields = cursor.fetchall()

    def generate(self):
        print("Table name: ", self.table)
        print("Fields:")
        for field in self.fields:
            print(field)

        ## Genera i files del model
        model = models.Models(self.table, self.fields, self.destination_root)
        model.Generate()