import sqlite3


class BaseDatos:
    
    def __init__(self):
        self.conector = sqlite3.connect('Hotel.sqlite')
        self.cursor = self.conector.cursor()
        
    def consulta(self, consulta):
        
        self.cursor.execute(consulta)
        return self.cursor