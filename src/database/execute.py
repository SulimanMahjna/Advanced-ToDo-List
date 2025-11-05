from src.database.connection import engine
class DBClient:
    def execute_all(self, query):
        with engine.begin() as connection:
            result = connection.execute(query).fetchall()
            return result


    
    def execute_one(self, password):
        with engine.begin() as connection:
            result = connection.execute(query).fetchone()
            return result


 