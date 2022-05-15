from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class FactionBaseData:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/factions/faction_base_data/#schema
    """
    __tablename__ = "faction_base_data"
    client_faction_id = Column(mysql.SMALLINT(display_width=6), nullable=False, primary_key=True, default=None)
    min = Column(mysql.SMALLINT(display_width=6), nullable=True, default=-2000)
    max = Column(mysql.SMALLINT(display_width=6), nullable=True, default=2000)
    unk_hero1 = Column(mysql.SMALLINT(display_width=6), nullable=True, default=None)
    unk_hero2 = Column(mysql.SMALLINT(display_width=6), nullable=True, default=None)
    unk_hero3 = Column(mysql.SMALLINT(display_width=6), nullable=True, default=None)


@mapper_registry.mapped
class FactionList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/factions/faction_list/#schema
    """
    __tablename__ = "faction_list"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    name = Column(mysql.VARCHAR(50), nullable=False)
    base = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)


@mapper_registry.mapped
class FactionListMod:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/factions/faction_list_mod/#schema
    """
    __tablename__ = "faction_list_mod"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    faction_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                        primary_key=True, unique=False, default=None)
    mod = Column(mysql.SMALLINT(display_width=6), nullable=False, default=None)
    mod_name = Column(mysql.VARCHAR(16), nullable=False, default=None)


@mapper_registry.mapped
class FactionValues:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/factions/faction_values/#schema
    """
    __tablename__ = "faction_values"
    char_id = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    faction_id = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    current_value = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    temp = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
