from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Fishing:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/fishing/
    """
    __tablename__ = "fishing"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    zoneid = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    itemid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    skill_level = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    chance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    npc_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    npc_chance = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items = relationship("Items", back_populates="fishing")
    zone = relationship("Zone", back_populates="fishing")
    npc_types = relationship("NPCTypes", back_populates="fishing")


@mapper_registry.mapped
class Forage:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/forage/
    """
    __tablename__ = "forage"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    zoneid = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    Itemid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    level = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    chance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(display_width=100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(display_width=100), nullable=True, default=None)

    items = relationship("Items", back_populates="forage", uselist=False)
    zone = relationship("Zone", back_populates="forage", uselist=False)


@mapper_registry.mapped
class TradeskillRecipe:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe/
    """
    __tablename__ = "tradeskill_recipe"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    name = Column(mysql.VARCHAR(display_width=64), nullable=False)
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
    content_flags = Column(mysql.VARCHAR(display_width=100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(display_width=100), nullable=True, default=None)


@mapper_registry.mapped
class TradeskillRecipeEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tradeskills/tradeskill_recipe_entries/
    """
    __tablename__ = "tradeskill_recipe_entries"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    recipe_id = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    successcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    failcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    componentcount = Column(mysql.TINYINT(display_width=2), nullable=False, default=1)
    salvagecount = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    iscontainer = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)

    tradeskill_recipe = relationship("TradeskillRecipe", back_populates="tradeskill_recipe_entries")
