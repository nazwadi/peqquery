from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base
from models.items import Items


class Loottable(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/loottable/

    Relationships:
        | Relationship Type | Local Key | Relates to Table  | Foreign Key |
        | ----------------- | --------- | ----------------  | ----------- |
        | Has-Many          | id        | loottable_entries | loottable_id |
        | Has-Many          | id        | npc_types         | loottable_id |
    """
    __tablename__ = "loottable"

    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Loottable Identifier"""
    name = Column(mysql.VARCHAR(255), nullable=False)
    """Name"""
    mincash = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Minimum Cash in Copper"""
    maxcash = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Maximum Cash in Copper"""
    avgcoin = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Average Coin in Copper"""
    done = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    """Done: 0 = False, 1 = True"""
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)

    loottable_entries = relationship("LoottableEntries")


class Lootdrop(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/lootdrop/

    Relationships:
        | Relationship Type | Local Key | Relates to Table  | Foreign Key |
        | ----------------- | --------- | ----------------  | ----------- |
        | Has-Many          | id        | lootdrop_entries  | lootdrop_id |
        | Has-Many          | id        | loottable_entries | loottable_id |
    """
    __tablename__ = "lootdrop"

    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Lootdrop Identifier"""
    name = Column(mysql.VARCHAR(255), nullable=False)
    """Name"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)


class LootdropEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/lootdrop_entries/

    Relationships:
        | Relationship Type | Local Key   | Relates to Table  | Foreign Key |
        | ----------------- | ---------   | ----------------  | ----------- |
        | One-to-One        | item_id     | items             | id          |
        | One-to-One        | lootdrop_id | lootdrop          | id          |
    """
    __tablename__ = "lootdrop_entries"

    lootdrop_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Lootdrop.id),
                         nullable=False, primary_key=True, default=0)
    """Lootdrop Identifier (see https://docs.eqemu.io/schema/loot/lootdrop/)"""
    item_id = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                     nullable=False, primary_key=True, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    item_charges = Column(mysql.SMALLINT(display_width=2, unsigned=True), nullable=False, default=1)
    """Item Charges"""
    equip_item = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    """Equip Item: 0 = False, 1 = True"""
    chance = Column(mysql.FLOAT, nullable=False, default=1)
    """Chance: 0 = Never, 100 = Always"""
    disabled_chance = Column(mysql.FLOAT, nullable=False, default=0)
    """Disabled Chance: 0 = Never, 100 = Always"""
    trivial_min_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    trivial_max_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    multiplier = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=1)
    """Multiplier"""
    npc_min_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    npc_max_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)

    items = relationship("Items", back_populates="lootdrop_entries")
    lootdrop = relationship("Lootdrop")


class LoottableEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/loottable_entries/

    Relationships:
        | Relationship Type | Local Key   | Relates to Table  | Foreign Key |
        | ----------------- | ---------   | ----------------  | ----------- |
        | Has-Many          | lootdrop_id | lootdrop_entries  | lootdrop_id |
    """
    __tablename__ = "loottable_entries"

    loottable_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Loottable.id),
                          nullable=False, primary_key=True, default=0)
    """Loottable Identifier (see https://docs.eqemu.io/schema/loot/loottable/)"""
    lootdrop_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(LootdropEntries.lootdrop_id),
                         nullable=False, primary_key=True, default=0)
    """Lootdrop Identifier (see https://docs.eqemu.io/schema/loot/lootdrop/)"""
    multiplier = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=1)
    """Multiplier"""
    droplimit = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    """Maximum Drops"""
    mindrop = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    """Minimum Drops"""
    probability = Column(mysql.FLOAT, nullable=False, default=100)
    """Probability: 0 = Never, 100 = Always"""

    lootdrop_entries = relationship("LootdropEntries")
    """
    Relationship Type: Has-Many, Local Key: lootdrop_id,
    Relates to Table: lootdrop_entries, Foreign Key: lootdrop_id
    """


class GlobalLoot(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/global_loot/
    """
    __tablename__ = "global_loot"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Global Loot Identifier"""
    description = Column(mysql.VARCHAR(255), nullable=True)
    """Description"""
    loottable_id = Column(ForeignKey(Loottable.id))
    """Loottable Identifier (see https://docs.eqemu.io/schema/loot/loottable/)"""
    enabled = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)  # Enabled: 0 = False, 1 = True
    """Enabled: 0 = False, 1 = True"""
    min_level = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Minimum Level"""
    max_level = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Maximum Level"""
    rare = Column(mysql.TINYINT(display_width=4), nullable=True)
    """Rare: 0 = False, 1 = True"""
    raid = Column(mysql.TINYINT(display_width=4), nullable=True)
    """Raid: 0 = False, 1 = True"""
    race = Column(mysql.MEDIUMTEXT, nullable=True)
    """Race (see https://docs.eqemu.io/server/npc/race-list), multiple races supported if"""
    class_column = Column(mysql.MEDIUMTEXT, name="class", nullable=True)
    """Class (see https://docs.eqemu.io/server/player/class-list), multiple classes supported if"""
    bodytype = Column(mysql.MEDIUMTEXT, nullable=True)
    """Body Type (see https://docs.eqemu.io/server/npc/body-types), multiple body types supported if"""
    zone = Column(mysql.MEDIUMTEXT, nullable=True)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list), multiple zones supported if"""
    hot_zone = Column(mysql.TINYINT(display_width=4), nullable=True)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)

    loottable = relationship("Loottable")
