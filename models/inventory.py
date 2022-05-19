from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .items import Items


@mapper_registry.mapped
class Inventory:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory/
    """
    __tablename__ = "inventory"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    slotid = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, primary_key=True, default=0)
    """Slot Identifier (see https://docs.eqemu.io/server/inventory/inventory-slots)"""
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Items.id),
                    nullable=True, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=True, default=0)
    """Charges"""
    color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Color"""
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 1"""
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 2"""
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 3"""
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 4"""
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    """Augment Slot 5"""
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
    """Augment Slot 6"""
    instnodrop = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    """No Drop: 0 = False, 1 = True"""
    custom_data = Column(mysql.TEXT, nullable=True, default=None)
    """Custom Data"""
    ornamenticon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Ornamentation Icon"""
    ornamentidfile = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Ornamentation Texture"""
    ornament_hero_model = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Ornamentation Hero's Forge Model"""

    items = relationship("Items", uselist=False)
    """Relationship Type: One-to-One, Local Key: itemid, Relates to Table: items, Foreign Key: id"""


@mapper_registry.mapped
class InventorySnapshots:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory_snapshots/
    """
    __tablename__ = "inventory_snapshots"
    time_index = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    """Inventory Snapshot Time Identifier"""
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    slotid = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, primary_key=True, default=0)
    """Slot Identifier (see https://docs.eqemu.io/server/inventory/inventory-slots)"""
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=True, default=0)
    """Charges"""
    color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Color"""
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 1"""
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 2"""
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 3"""
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    """Augment Slot 4"""
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    """Augment Slot 5"""
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
    """Augment Slot 6"""
    instnodrop = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    """No Drop: 0 = False, 1 = True"""
    custom_data = Column(mysql.TEXT, nullable=True, default=None)
    """Custom Data"""
    ornamenticon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Ornamentation Icon"""
    ornamentidfile = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Ornamentation Texture"""
    ornament_hero_model = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Ornamentation Hero's Forge Model"""


@mapper_registry.mapped
class InventoryVersions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory_versions/
    """
    __tablename__ = "inventory_versions"
    version = Column(mysql.INTEGER(display_width=11, unsigned=True), primary_key=True, nullable=False, default=0)
    """Inventory Version Identifier; Primary Key not set in actual SQL"""
    step = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Step"""
    bot_step = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Bot Step"""
