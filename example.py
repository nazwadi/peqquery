#!/usr/bin/env python3
from dotenv import dotenv_values
from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.sql import select

from models import *
from queries import drop_chance_of_item_by_id

config = dotenv_values(".env")


def get_npc(npc_name: str) -> str:
    with engine.connect() as conn:
        npc_name = npc_name.replace(" ", "_")
        s = select(NPCTypes).where(NPCTypes.name == npc_name)
        res = conn.execute(s)
    return res


def get_account():
    with engine.connect() as conn:
        s = select(Account)
        res = conn.execute(s)
        return res


if __name__ == "__main__":
    #    metadata_obj = MetaData()
    #    npc_types = Table('npc_types', metadata_obj, autoload_with=engine)
    #    print([c.name for c in npc_types.columns])
    connection_string = "mysql+pymysql://"
    connection_string += config["PEQ_DB_USERNAME"]
    connection_string += ":"
    connection_string += config["PEQ_DB_PASSWORD"]
    connection_string += "@"
    connection_string += config["PEQ_DB_HOST"]
    connection_string += "/"
    connection_string += config["PEQ_DB_DATABASE"]
    engine = create_engine(connection_string, future=True)
#    result = get_npc("Trakanon")
    result = drop_chance_of_item_by_id(engine, 19285)
    for i in result:
        print(i)
