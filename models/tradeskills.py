from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .items import Items
from .zone import Zone
from .npcs import NPCTypes


@mapper_registry.mapped
class Fishing:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/fishing/
    """
    __tablename__ = "fishing"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Fishing Identifier"""
    zoneid = Column(mysql.INTEGER(display_width=4), ForeignKey(Zone.zoneidnumber), nullable=False, default=0)
    """Zone Identifier"""
    itemid = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id), nullable=False, default=0)
    """Item Identifier"""
    skill_level = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Skill Level"""
    chance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Chance: 0 = Never, 100 = Always"""
    npc_id = Column(mysql.INTEGER(display_width=11), ForeignKey(NPCTypes.id), nullable=False, default=0)
    """NPC Type Identifier"""
    npc_chance = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """NPC Chance: 0 = Never, 100 = Always"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items = relationship("Items", back_populates="fishing", uselist=False)
    """Relationship Type: One-to-One, Local Key: itemid, Relates to Table: items, Foreign Key: id"""
    zone = relationship("Zone", back_populates="fishing", uselist=False)
    """Relationship Type: One-to-One, Local Key: zoneid, Relates to Table: zone, Foreign Key: zoneidnumber"""
    npc_types = relationship("NPCTypes", back_populates="fishing", uselist=False)
    """Relationship Type: One-to-One, Local Key: npc_id, Relates to Table: npc_types, Foreign Key: id"""


@mapper_registry.mapped
class Forage:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/forage/
    """
    __tablename__ = "forage"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Forage Identifier"""
    zoneid = Column(mysql.INTEGER(display_width=4), ForeignKey(Zone.zoneidnumber), nullable=False, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    Itemid = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id), nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    level = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Level"""
    chance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Chance: 0 = Never, 100 = Always"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items = relationship("Items", back_populates="forage", uselist=False)
    """Relationship Type: One-to-One, Local Key: Itemid, Relates to Table: items, Foreign Key: id"""
    zone = relationship("Zone", back_populates="forage", uselist=False)
    """Relationship Type: One-to-One, Local Key: zoneid, Relates to Table: zone, Foreign Key: zoneidnumber"""


@mapper_registry.mapped
class TradeskillRecipe:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe/
    """
    __tablename__ = "tradeskill_recipe"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    name = Column(mysql.VARCHAR(64), nullable=False)
    tradeskill = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    skillneeded = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    trivial = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    nofail = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    replace_container = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    notes = Column(mysql.TINYTEXT, nullable=True, default=None)
    must_learn = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    quest = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    enabled = Column(mysql.TINYINT(display_width=1), nullable=False, default=1)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)


@mapper_registry.mapped
class TradeskillRecipeEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe_entries/
    """
    __tablename__ = "tradeskill_recipe_entries"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    recipe_id = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    successcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    failcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    componentcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=1)
    salvagecount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    iscontainer = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)

    tradeskill_recipe = relationship("TradeskillRecipe", back_populates="tradeskill_recipe_entries")
