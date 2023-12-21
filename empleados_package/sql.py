from sqlalchemy import create_engine, text

def conexion_sql(usuario="root", password, db_name):

    """
    Establece una conexión a una base de datos MySQL utilizando SQLAlchemy.

    Parámetros:
    - usuario (str): Nombre de usuario para la conexión a MySQL. Por defecto, se usa "root".
    - password (str): Contraseña para la conexión a MySQL.
    - db_name (str): Nombre de la base de datos a la que se desea conectar.

    Retorna:
    - connection: Objeto de conexión a la base de datos.

    Comentarios:
    - Esta función utiliza la biblioteca SQLAlchemy para establecer una conexión
      a una base de datos MySQL. La URL de conexión se construye utilizando el
      nombre de usuario proporcionado (por defecto "root"), la contraseña y el
      nombre de la base de datos especificado. Se recomienda cerrar la conexión
      utilizando el método close() del objeto de conexión después de realizar las
      operaciones necesarias en la base de datos.
    """

    url = f"mysql+pymysql://{usuario}:{password}@localhost/{db_name}"
    engine = create_engine(url)
    connection = engine.connect()

    return connection