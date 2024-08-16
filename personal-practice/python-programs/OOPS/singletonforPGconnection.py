import psycopg2
class Postgres:
    __instance = None
    
    @staticmethod
    def get_instance():
        if Postgres.__instance is None:
            Postgres()
        return Postgres.__instance
    
    def __init__(self):
        
        if Postgres.__instance is not None:
            raise Exception("This is a sinleton class for Postgres connection use get_instance() method to access object!")
        else:
            
            self.connection = psycopg2.connect("host", "port", "database", "user", "password")
            Postgres.__instance = self
            
    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        self.connection.close()
        

postgres = Postgres.get_instance()
connection = postgres.get_connection()
cursor = connection.cursor()
cursor.execute("select * from table")
result = cursor.fetcall()
postgres.close_connection()        
            