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
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    itemid = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id), nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    skill_level = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Skill Level"""
    chance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Chance: 0 = Never, 100 = Always"""
    npc_id = Column(mysql.INTEGER(display_width=11), ForeignKey(NPCTypes.id), nullable=False, default=0)
    """NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/)"""
    npc_chance = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """NPC Chance: 0 = Never, 100 = Always"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items = relationship("Items", back_populates="fishing", uselist=False)
    """Relationship Type: One-to-One, Local Key: itemid, Relates to Table: items, Foreign Key: id"""
    zone = relationship("Zone", uselist=False)
    """Relationship Type: One-to-One, Local Key: zoneid, Relates to Table: zone, Foreign Key: zoneidnumber"""
    npc_types = relationship("NPCTypes", uselist=False)
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
    zone = relationship("Zone", uselist=False)
    """Relationship Type: One-to-One, Local Key: zoneid, Relates to Table: zone, Foreign Key: zoneidnumber"""


@mapper_registry.mapped
class TradeskillRecipe:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe/
    """
    __tablename__ = "tradeskill_recipe"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Tradeskill Recipe Identifier"""
    name = Column(mysql.VARCHAR(64), nullable=False)
    """Recipe Name"""
    tradeskill = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Tradeskill (see https://docs.eqemu.io/server/player/skills)"""
    skillneeded = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Skill Level Needed"""
    trivial = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Trivial Skill Level"""
    nofail = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """No Fail: 0 = False, 1 = True"""
    replace_container = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Replace Container: 0 = False, 1 = True"""
    notes = Column(mysql.TINYTEXT, nullable=True, default=None)
    """Notes"""
    must_learn = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Must Learn: 0 = False, 1 = True"""
    quest = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Quest Controlled: 0 = False, 1 = True"""
    enabled = Column(mysql.TINYINT(display_width=1), nullable=False, default=1)
    """Enabled: 0 = False, 1 = True"""
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
    """Unique Tradeskill Recipe Entry Identifier"""
    recipe_id = Column(mysql.INTEGER(display_width=11), ForeignKey(TradeskillRecipe.id),
                       nullable=False, unique=False, primary_key=True, default=0)
    """Unique Tradeskill Recipe Identifier (see https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe/)"""
    item_id = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                     nullable=False, unique=False, primary_key=True, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    successcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    """Success Count"""
    failcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    """Fail Count"""
    componentcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=1)
    """Component Count"""
    salvagecount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    """Salvage Count"""
    iscontainer = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Is Container: 0 = False, 1 = True"""

    tradeskill_recipe = relationship("TradeskillRecipe")
    """Relationship Type: One-to-One, Local Key: recipe_id, Relates to Table: tradeskill_recipe, Foreign Key: id"""
