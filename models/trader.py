from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class Trader:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/trader/trader/
    """
    __tablename__ = "trader"
    char_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    """Unique Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    item_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    serialnumber = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Serial Number"""
    charges = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Charges"""
    item_cost = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Item Cost"""
    slot_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    """Slot Identifier (see https://docs.eqemu.io/server/inventory/inventory-slots)"""


@mapper_registry.mapped
class TraderAudit:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/trader/trader_audit/
    """
    __tablename__ = "trader_audit"
    time = Column(mysql.DATETIME, nullable=False, primary_key=True, default="0000-00-00 00:00:00")
    """Primary Key not actually set in SQL"""
    seller = Column(mysql.VARCHAR(64), primary_key=True, nullable=False)
    """Primary Key not actually set in SQL"""
    buyer = Column(mysql.VARCHAR(64), primary_key=True, nullable=False)
    """Primary Key not actually set in SQL"""
    itemname = Column(mysql.VARCHAR(64), primary_key=True, nullable=False)
    """Item Name (see https://docs.eqemu.io/schema/items/items/); Primary Key not actually set in SQL"""
    quantity = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=False, default=0)
    """Primary Key not actually set in SQL"""
    totalcost = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=False, default=0)
    """Primary Key not actually set in SQL"""
    trantype = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key not actually set in SQL"""
