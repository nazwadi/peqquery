from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker)


config = dotenv_values(".env")

connection = list()
connection.append("mysql+pymysql://")
connection.append(config["PEQ_DB_USERNAME"])
connection.append(":")
connection.append(config["PEQ_DB_PASSWORD"])
connection.append("@")
connection.append(config["PEQ_DB_HOST"])
connection.append("/")
connection.append(config["PEQ_DB_DATABASE"])
connection_string = ''.join(connection)

engine = create_engine(connection_string, future=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
