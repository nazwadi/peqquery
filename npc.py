#!/usr/bin/env python3
import argparse
import logging
import math
import sys

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from sqlalchemy.engine.cursor import CursorResult

from models import *


config = dotenv_values(".env")


def get_npc(npc_name: str, zone_short_name: str, show_sql: bool) -> CursorResult:
    """
    Returns a record for all NPCs matching a specific name.  If a zone
    short name is specified, the query will be filtered by NPCs that spawn
    in that zone.

    @param npc_name
    @param zone_short_name
    @param show_sql

    @return the query result cursor
    """
    with engine.connect() as conn:
        npc_name = npc_name.replace(" ", "_")
        if zone_short_name is not None:
            stmt = select(NPCTypes.name, NPCTypes.loottable_id, SpawnEntry.spawngroupID, Zone.long_name, Zone.short_name) \
                .join(SpawnEntry, NPCTypes.id == SpawnEntry.npcID) \
                .join(Spawn2, SpawnEntry.spawngroupID == Spawn2.spawngroupID) \
                .join(Zone, Spawn2.zone == Zone.short_name) \
                .where(NPCTypes.name == npc_name) \
                .where(Zone.short_name == zone_short_name) \
                .where(NPCTypes.race != '127') \
                .where(NPCTypes.race != '240')
        else:
            stmt = select(NPCTypes.name, NPCTypes.loottable_id, SpawnEntry.spawngroupID, Zone.long_name, Zone.short_name) \
                .join(SpawnEntry, NPCTypes.id == SpawnEntry.npcID) \
                .join(Spawn2, SpawnEntry.spawngroupID == Spawn2.spawngroupID) \
                .join(Zone, Spawn2.zone == Zone.short_name) \
                .where(NPCTypes.name == npc_name) \
                .where(NPCTypes.race != '127') \
                .where(NPCTypes.race != '240')
        if show_sql:
            logging.info(stmt)
        res = conn.execute(stmt)
    return res


def get_npc_special_attacks(npc_name: str, zone_short_name: str) -> CursorResult:
    with engine.connect() as conn:
        npc_name = npc_name.replace(" ", "_")
        stmt = select(NPCTypes.special_abilities) \
            .where(NPCTypes.name == npc_name)
        res = conn.execute(stmt)
    return res


def get_npc_known_loot_table_id(loot_table_id: str) -> None:
    """
    Print known loot

    This function first queries a loot table id from an NPC name,
    then it lists all loot table entries for that loot table.

    For each loot table entry, it lists the loot drop table and the
    loot drop entries.
    """
    with Session(engine) as session:
        stmt = select(LoottableEntries).where(LoottableEntries.loottable_id == loot_table_id)
        loot_table_entries = session.execute(stmt)
        for row in loot_table_entries:
            row = row[0]
            stmt = select(LootdropEntries).where(LootdropEntries.lootdrop_id == row.lootdrop_id)
            loot_drop_entries = session.execute(stmt)
            for lde in loot_drop_entries:
                lde = lde[0]
                stmt = select(Items.Name).where(Items.id == lde.item_id)
                item_name = session.execute(stmt).first()[0]
                print("* [[{}]]".format(item_name, lde.item_id, lde.chance))
            print()


def get_npc_merchant_list(merchant_id: int) -> list:
    with Session(engine) as session:
        stmt = select(MerchantList, Items.Name, Items.price, Items.icon)\
               .join(MerchantList.items).where(MerchantList.merchantid == merchant_id).order_by(Items.Name)
        db_result = session.execute(stmt)
        merchant_list = list()
        for row in db_result:
            merchant_list.append(row)
    return merchant_list


def display_mediawiki_merchant_list(merchant_list: list) -> None:
    """Displays Mediawiki Text for an NPC Page Merchant List"""
    string_list = list()
    string_list.append("\n=== Items Sold ===\n")
    string_list.append("{{MerchantTableHeader}}")
    string_list.append("{{MerchantHeaderRow|hasIcon=true}}\n")
    with Session(engine) as session:
        for mlist_entry in merchant_list:
            # Item price is stored in units of Copper
            platinum = math.floor(mlist_entry.price / 1000)
            gold = math.floor((mlist_entry.price % 1000) / 100)
            silver = math.floor((mlist_entry.price % 100) / 10)
            copper = mlist_entry.price % 10

            string_list.append("{{MerchantRow")
            string_list.append("|iconNumber={}".format(mlist_entry.icon))
            string_list.append("|itemName=[[{}]]".format(mlist_entry.Name))
            string_list.append("|platinum={}".format(platinum))
            string_list.append("|gold={}".format(gold))
            string_list.append("|silver={}".format(silver))
            string_list.append("|copper={}".format(copper))
            string_list.append("|level=--")
            string_list.append("}}")
    string_list.append("{{MerchantTableFooter}}")
    page_text = '\n'.join(string_list)
    print(page_text)


def get_npc_loot_by_name(npc_name: str) -> None:
    with Session(engine) as session:
        npc_name = npc_name.replace(" ", "_")
        stmt = select(NPCTypes.loottable_id).where(NPCTypes.name == npc_name)
        loot_table_id = session.scalars(stmt).first()
        if loot_table_id is not None:
            stmt = select(Loottable).where(Loottable.id == loot_table_id)
            res = session.execute(stmt).first()
            for loottable in res:
                lt = loottable
                print("Loot Table {} '{}'".format(lt.id, lt.name))
                print("===========================")
                print("Cash Loot")
                print("\tMin Cash: {}\n\tMax Cash: {}\n\tDone: {}".format(lt.mincash, lt.maxcash, lt.avgcoin, lt.done))
                print("Content Control")
                print("\tMin Expansion: {}\n\tMax Expansion: {}\n\tContent Flags: {}\n\tContent Flags Disabled: {}".format(lt.min_expansion, lt.max_expansion, lt.content_flags, lt.content_flags_disabled))
                print("===========================")
                stmt = select(LoottableEntries).where(LoottableEntries.loottable_id == loot_table_id)
                loot_table_entries = session.execute(stmt)
                for row in loot_table_entries:
                    row = row[0]
                    print("------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("| Loot Table Entry ==> Loottable ID: {}\tLootdrop ID: {}\tMinDrop: {}\tDrop Limit: {}\tMultiplier: {}\tProbability: {}\t|".format(row.loottable_id, row.lootdrop_id, row.mindrop, row.droplimit, row.multiplier, row.probability))
                    print("------------------------------------------------------------------------------------------------------------------------------------------------")
                    stmt = select(Lootdrop).where(Lootdrop.id == row.lootdrop_id)
                    lootdrop = session.execute(stmt)
                    for ld in lootdrop:
                        ld = ld[0]
                        print("\tLoot Drop ==> id: {}\tname: {}, Min Expansion: {}, Max Expansion: {}, Content Flags: {}, Content Flags Disabled: {}".format(ld.id, ld.name, ld.min_expansion, ld.max_expansion, ld.content_flags, ld.content_flags_disabled))
                        stmt = select(LootdropEntries).where(LootdropEntries.lootdrop_id == row.lootdrop_id)
                        loot_drop_entries = session.execute(stmt)
                        print("{:>25}{:>41}{:>5}{:>22}{:>20}{:>18}{:>18}{:>23}{:>10}{:>15}{:>15}{:>15}".format("Lootdrop ID", "Item Name", "(ID)", "Item Charges", "Equip Item", "Chance", "Disabled Chance", "TMin", "TMax", "NPCMin", "NPCMax", "Multiplier"))
                        print("{:>25}{:>46}{:>22}{:>20}{:>18}{:>18}{:>23}{:>10}{:>15}{:>15}{:>15}".format("===========", "==============", "============", "==========", "======", "===============", "====", "====", "======", "======", "=========="))
                        for lde in loot_drop_entries:
                            lde = lde[0]
                            equip = True if lde.equip_item else False
                            stmt = select(Items.Name).where(Items.id == lde.item_id)
                            item_name = session.execute(stmt).first()[0]
                            print("{:>25d}{:>41s} ({:=5d}){:>19d}{:>20d}{:>18}{:>18}{:>23}{:>10}{:>15}{:>15}{:>15}".format(lde.lootdrop_id, item_name, lde.item_id, lde.item_charges, equip, lde.chance, lde.disabled_chance, lde.trivial_min_level, lde.trivial_max_level, lde.multiplier, lde.npc_min_level, lde.npc_max_level))
                    print()


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
    parser.add_argument('--name', action='store', type=str, help="name of the NPC")
    parser.add_argument('--zone', action='store', type=str, help="zone short name the NPC is found in")
    parser.add_argument('--show-sql', action='store_true', help="show SQL Query")
    parser.add_argument('--loot-table-id', action='store', type=str, help="find loot table by loot id")
    parser.add_argument('--special-attacks', action='store_true', help="get npc special attacks")
    parser.add_argument('--merchant_id', action='store', type=int, help="find merchant list by merchant id")
    options = parser.parse_args()
    if options.name:
        if options.zone:
            result = get_npc(options.name, options.zone, options.show_sql)
        else:
            result = get_npc(options.name, None, options.show_sql)
        print("{:<10} {:45} {:<25} {:<25} {:<25} {:<25}".format("Index", "NPC_Name", "Loottable_ID", "SpawnGroup_ID", "Zone_Short_Name", "Zone_Long_Name"))
        for index, value in enumerate(result):
            print("{:<10} {:<45} {:<25} {:<25} {:<25} {:<25}".format(index, value['name'], value['loottable_id'], value['spawngroupID'], value['short_name'], value['long_name']))
    if options.loot_table_id:
        get_npc_known_loot_table_id(options.loot_table_id)
    if options.special_attacks:
        result = get_npc_special_attacks(options.name, options.zone)
        for index, value in enumerate(result):
            print(value)
    if options.merchant_id:
        mlist = get_npc_merchant_list(options.merchant_id)
        display_mediawiki_merchant_list(mlist)
