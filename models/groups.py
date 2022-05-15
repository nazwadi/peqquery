from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from meta import mapper_registry

from .characters import CharacterData


@mapper_registry.mapped
class GroupId:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/groups/group_id/
    """
    __tablename__ = "group_id"
    groupid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=None)
    """Unique Group Identifier"""
    charid = Column(mysql.INTEGER(display_width=4), ForeignKey(CharacterData.id), primary_key=True,
                    nullable=False, default=None)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    name = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Name"""
    ismerc = Column(mysql.TINYINT(display_width=3), nullable=False, primary_key=True, default=0)
    """Is Mercenary: 0 = False, 1 = True"""


@mapper_registry.mapped
class GroupLeaders:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/groups/group_leaders/
    """
    __tablename__ = "group_leaders"
    gid = Column(mysql.INTEGER(display_width=4), ForeignKey(GroupId.groupid), primary_key=True,
                 nullable=False, default=0)
    """Group Identifier (see https://docs.eqemu.io/schema/groups/group_id/)"""
    leadername = Column(mysql.VARCHAR(64), nullable=False)
    """Leader Name"""
    marknpc = Column(mysql.VARCHAR(64), nullable=False)
    """Mark NPC: 0 = False, 1 = True"""
    leadershipaa = Column(mysql.TINYBLOB, nullable=True, default=None)
    """Leadership AA"""
    maintank = Column(mysql.VARCHAR(64), nullable=False)
    """Main Tank: 0 = False, 1 = True"""
    assist = Column(mysql.VARCHAR(64), nullable=False)
    """Assist: 0 = False, 1 = True"""
    puller = Column(mysql.VARCHAR(64), nullable=False)
    """Puller: 0 = False, 1 = True"""
    mentoree = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Mentoree: 0 = False, 1 = True"""
    mentor_percent = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Main Tank: 0 = None, 100 = Max"""
