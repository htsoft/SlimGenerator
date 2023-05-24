import entity
import repository
import action

class Scaffolder:
    def __init__(self, connection, table, destination_root) -> None:
        self.entity = entity.Entita(connection,table,destination_root)
        self.repository = repository.Repository(connection,table,destination_root)
        self.action = action.GenericAction(connection,table,destination_root)

    def generate(self):
        self.entity.generate()
        self.repository.generate()
        self.action.generate()