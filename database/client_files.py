from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class BaseData:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/client-files/base_data/
    """
    __tablename__ = "base_data"
    level = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    _class = Column("class", mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                    primary_key=True, default=None)
    hp = Column(mysql.DOUBLE, nullable=False, default=None)
    mana = Column(mysql.DOUBLE, nullable=False, default=None)
    end = Column(mysql.DOUBLE, nullable=False, default=None)
    unk1 = Column(mysql.DOUBLE, nullable=False, default=None)
    unk2 = Column(mysql.DOUBLE, nullable=False, default=None)
    hp_fac = Column(mysql.DOUBLE, nullable=False, default=None)
    mana_fac = Column(mysql.DOUBLE, nullable=False, default=None)
    end_fac = Column(mysql.DOUBLE, nullable=False, default=None)


@mapper_registry.mapped
class DbStr:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/client-files/db_str/
    """
    __tablename__ = "db_str"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None)
    type = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None)
    value = Column(mysql.TEXT, nullable=False, default=None)


@mapper_registry.mapped
class SkillCaps:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/client-files/skill_caps/
    """
    __tablename__ = "skill_caps"
    skillID = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    _class = Column("class", mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    cap = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    class_ = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
