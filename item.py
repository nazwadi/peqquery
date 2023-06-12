#!/usr/bin/env python3
import argparse
import logging
import sys
import webbrowser

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.engine.cursor import CursorResult

from eqdata import player_classes
from eqdata import player_races
from eqdata import item_slots
from eqdata import item_types
from eqdata import item_sizes

from models import *

config = dotenv_values(".env")


def decode_slot_bitmask(bitmask: int) -> list:
    """

    """
    slots = list()
    index = 0
    while bitmask >= 1:
        if bitmask % 2:
            slots.append(item_slots[index].name)
        bitmask = bitmask // 2
        index = index + 1
    return slots


def decode_race_class_bitmask(bitmask: int, list_namedtuples: list) -> list:
    """
    Returns a list of race/class abbreviations given a bitmask and list of
    namedtuples

    @param bitmask
    @param list_namedtuples
    """
    ret = list()
    if bitmask == 65535:
        ret.append("ALL")
        return ret
    index = 0
    while bitmask >= 1:
        if bitmask % 2:
            ret.append(list_namedtuples[index].name)
        bitmask = bitmask // 2
        index = index + 1
    return ret


def find_item_by_id(item_id: str, show_sql: bool) -> CursorResult:
    """
    Find an item by its item id
    @param item_id
    @param show_sql
    """
    with engine.connect() as conn:
        stmt = select(Items).where(Items.id == item_id)
        if show_sql:
            logging.info(stmt)
        result = conn.execute(stmt)
        return result


def print_item_info(res: CursorResult):
    """
    Print Item Information to stdout
    """
    print("{}".format(i.Name))
    print("({}) - id: {}\n".format(i.lore, i.id))
    if i.loregroup == -1:
        print("LORE ITEM".format(i.loregroup), end=' ')
    if i.nodrop == 0:
        print("NO DROP".format(i.nodrop), end=' ')
    if i.magic == 1:
        print("MAGIC ITEM")
    if i.classes:
        print("Classes: ", end='')
        for index, value in enumerate(decode_race_class_bitmask(i.classes, player_classes)):
            print(value, end=' ')
    if i.races:
        print("\nRaces: ", end='')
        for index, value in enumerate(decode_race_class_bitmask(i.races, player_races)):
            print(value, end=' ')
    if i.slots:
        print("\nSlot: ", end='')
        for index, value in enumerate(decode_slot_bitmask(i.slots)):
            print(value, end=' ')
    if i.itemtype:
        print("\nItem Type: ", end='')
        print(item_types[i.itemtype].type)
    if i.size:
        print("\nSize: ", end='')
        print(item_sizes[i.size].size, end='\t')
    if i.ac:
        print("AC: {}".format(i.ac))
    if i.weight:
        print("Weight: {}".format(i.weight), end='\t')
    if i.hp:
        print("HP: {}".format(i.hp))
    if i.mana:
        print("Mana: {}".format(i.mana))

    # TODO: Display item stats

    """Price in Copper"""
    print("Value: {} cp".format(i.price))


if __name__ == "__main__":
    connection_string = "mysql+pymysql://"
    connection_string += config["PEQ_DB_USERNAME"]
    connection_string += ":"
    connection_string += config["PEQ_DB_PASSWORD"]
    connection_string += "@"
    connection_string += config["PEQ_DB_HOST"]
    connection_string += "/"
    connection_string += config["PEQ_DB_DATABASE"]
    engine = create_engine(connection_string, future=True)

    # Init the example's logger theme
    handler = logging.StreamHandler(sys.stderr)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="Provide an NPC name")
    parser.add_argument('--item-id', action='store', type=str, help="name of the NPC")
    parser.add_argument('--show-sql', action='store_true', help="show SQL Query")
    parser.add_argument('--show-lucy', action='store_true', help="show SQL Query")
    options = parser.parse_args()
    if options.show_lucy:
        webbrowser.open("https://lucy.allakhazam.com/item.html?id=" + options.item_id)
    if options.item_id:
        res = find_item_by_id(options.item_id, options.show_sql)
        for i in res:
            print_item_info(res)
