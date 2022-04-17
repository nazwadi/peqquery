from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

from items import Item

mapper_registry = registry()


@mapper_registry.mapped
class Loottable:
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
    name = Column(mysql.VARCHAR(255), nullable=False)
    mincash = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)  # Min. Cash in Copper
    maxcash = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)  # Max. Cash in Copper
    avgcoin = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)  # Avg. Coin in Copper
    done = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)        # Done: 0 = False, 1 = True
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)


@mapper_registry.mapped
class Lootdrop:
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
    name = Column(mysql.VARCHAR(255), nullable=False)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)


@mapper_registry.mapped
class LoottableEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/loottable_entries/

    Relationships:
        | Relationship Type | Local Key   | Relates to Table  | Foreign Key |
        | ----------------- | ---------   | ----------------  | ----------- |
        | Has-Many          | lootdrop_id | lootdrop_entries  | lootdrop_id |
    """
    __tablename__ = "loottable_entries"

    loottable_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey('loottable.id'),
                          nullable=False, primary_key=True, default=0)
    lootdrop_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey('lootdrop_entries.lootdrop_id'),
                         nullable=False, primary_key=True, default=0)
    multiplier = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=1)
    droplimit = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)  # Maximum Drops
    mindrop = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)    # Minimum Drops
    probability = Column(mysql.FLOAT, nullable=False, default=100)  # Probability: 0 = Never, 100 = Always

    lootdrop_entries = relationship("LootdropEntries", back_populates="loottable_entries")


@mapper_registry.mapped
class LootdropEntries:
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
    item_id = Column(mysql.INTEGER(display_width=11), ForeignKey(Item.id),
                     nullable=False, primary_key=True, default=0)
    item_charges = Column(mysql.SMALLINT(display_width=2, unsigned=True), nullable=False, default=1)

    # Equip Item: 0 = False, 1 = True
    equip_item = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)

    chance = Column(mysql.FLOAT, nullable=False, default=1)        # Chance: 0 = Never, 100 = Always
    disabled_chance = Column(mysql.FLOAT, nullable=False, default=0)  # Disabled Chance: = 0 Never, 100 = Always
    trivial_min_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    trivial_max_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    multiplier = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=1)
    npc_min_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    npc_max_level = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class GlobalLoot:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loot/global_loot/
    """
    __tablename__ = "global_loot"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    description = Column(mysql.VARCHAR(255), nullable=True)
    loottable_id = Column(ForeignKey(Loottable.id))
    enabled = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)  # Enabled: 0 = False, 1 = True
    min_level = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max_level = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    rare = Column(mysql.TINYINT(display_width=4), nullable=True)
    raid = Column(mysql.TINYINT(display_width=4), nullable=True)
    race = Column(mysql.MEDIUMTEXT, nullable=True)
    class_column = Column(mysql.MEDIUMTEXT, name="class", nullable=True)
    bodytype = Column(mysql.MEDIUMTEXT, nullable=True)
    zone = Column(mysql.MEDIUMTEXT, nullable=True)
    hot_zone = Column(mysql.TINYINT(display_width=4), nullable=True)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)
