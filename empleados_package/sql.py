import sqlalchemy as alch
from sqlalchemy.exc import SQLAlchemyError # Import the necessary exception

class Cargar:
    
    def __init__(self, nombre_bbdd, contraseña):
        self.nombre_bbdd = nombre_bbdd
        self.contraseña = contraseña

    def conexion_servidor(self): 
        url = f"mysql+pymysql://root:{self.contraseña}@localhost/{self.nombre_bbdd}"
        engine = alch.create_engine(url)
        connection = engine.connect()
        return connection

    def crear_bbdd(self):
        engine = self.conexion_servidor()
        try:
            engine.execute(f"CREATE DATABASE IF NOT EXISTS {self.nombre_bbdd};")
        except:
            print("La BBDD ya existe")

    def crear_schema(self):
        engine = self.conexion_servidor()
        try:
            engine.execute(f"CREATE SCHEMA IF NOT EXISTS {self.nombre_bbdd} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;")
        except:
            print("El schema ya existe")

    def conexion_base_datos(self):
        # Use the same method to create the engine
        conexion2 = f"mysql+pymysql://root:{self.contraseña}@localhost/{self.nombre_bbdd}"
        return alch.create_engine(conexion2)

    def crear_insertar_tabla(self, query):
        try:
            with self.conexion_base_datos().begin() as conn:
                conn.execute(query)
        except SQLAlchemyError as e:
            error = str(e)
            return error
