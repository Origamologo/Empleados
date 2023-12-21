from sqlalchemy import create_engine, text

def conexion_sql(password, db_name):

    url = f"mysql+pymysql://root:{password}@localhost/{db_name}"
    engine = create_engine(url)
    connection = engine.connect()

    return connection