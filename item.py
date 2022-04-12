from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Item:
    __table_name = "item"

    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")


@mapper_registry.mapped
class ItemTick:
    """
    EQEMU Docs URL:  https://docs.eqemu.io/schema/items/item_tick/
    """
    __tablename__ = "item_tick"

    it_itemid = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_chance = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_level = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    it_qglobal = Column(mysql.VARCHAR(50), nullable=False)
    it_bagslot = Column(mysql.TINYINT(display_width=4), nullable=False)
