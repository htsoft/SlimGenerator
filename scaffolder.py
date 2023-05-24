import entity
import repository

class Scaffolder:
    def __init__(self, connection, table, destination_root) -> None:
        self.entity = entity.Entita(connection,table,destination_root)
        self.repository = repository.Repository(connection,table,destination_root)

    def generate(self):
        self.entity.generate()
        self.repository.generate()