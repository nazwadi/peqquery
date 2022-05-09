from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Inventory:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory/
    """
    __tablename__ = "inventory"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slotid = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=True, default=0)
    color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
    instnodrop = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    custom_data = Column(mysql.TEXT, nullable=True, default=None)
    ornamenticon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ornamentidfile = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ornament_hero_model = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)

    items = relationship("Items", back_populates="inventory", uselist=False)


@mapper_registry.mapped
class InventorySnapshots:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory_snapshots/
    """
    __tablename__ = "inventory_snapshots"
    time_index = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slotid = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=True, default=0)
    color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
    instnodrop = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    custom_data = Column(mysql.TEXT, nullable=True, default=None)
    ornamenticon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ornamentidfile = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ornament_hero_model = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class InventoryVersions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/inventory/inventory_versions/
    """
    __tablename__ = "inventory_versions"
    version = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    step = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    bot_step = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
