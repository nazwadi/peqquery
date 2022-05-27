from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base
from .characters import CharacterData
from .groups import GroupId


class RaidDetails(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/raids/raid_details/
    """
    __tablename__ = "raid_details"
    raidid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    """Unique Raid Identifier"""
    loottype = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Loot Type"""
    locked = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Locked: 0 = False, 1 = True"""
    motd = Column(mysql.VARCHAR(1024), nullable=True, default=None)
    """Message of the Day"""

    raid_leaders = relationship("RaidLeaders")
    raid_members = relationship("RaidMembers")


class RaidLeaders(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/raids/raid_leaders/
    """
    __tablename__ = "raid_leaders"
    gid = Column(mysql.INTEGER(display_width=4, unsigned=True),
                 ForeignKey(GroupId.groupid), primary_key=True, nullable=False, default=None)
    """Group Identifier (see https://docs.eqemu.io/schema/groups/group_id/); Primary Key not set in actual SQL"""
    rid = Column(mysql.INTEGER(display_width=4, unsigned=True),
                 ForeignKey(RaidDetails.raidid), primary_key=True, nullable=False, default=None)
    """Raid Identifier (see https://docs.eqemu.io/schema/raids/raid_details/); Primary Key not set in actual SQL"""
    marknpc = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Mark NPC: 0 = False, 1 = True"""
    maintank = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Main Tank: 0 = False, 1 = True"""
    assist = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Assist: 0 = False, 1 = True"""
    puller = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Puller: 0 = False, 1 = True"""
    leadershipaa = Column(mysql.TINYBLOB, nullable=False, default=None)
    """Leadership AA"""
    mentoree = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Mentoree: 0 = False, 1 = True"""
    mentor_percent = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Mentor Percent: 0 = None, 100 = Max"""


class RaidMembers(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/raids/raid_members/
    """
    __tablename__ = "raid_members"
    raidid = Column(mysql.INTEGER(display_width=4), ForeignKey(RaidDetails.raidid), nullable=False, default=0)
    """Raid Identifier (see https://docs.eqemu.io/schema/raids/raid_details/)"""
    charid = Column(mysql.INTEGER(display_width=4), ForeignKey(CharacterData.id),
                    nullable=False, primary_key=True, default=0)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    groupid = Column(mysql.INTEGER(display_width=4, unsigned=True), ForeignKey(GroupId.groupid),
                     nullable=False, default=0)
    """Group Identifier (see https://docs.eqemu.io/schema/groups/group_id/)"""
    _class = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Class (see https://docs.eqemu.io/server/player/class-list)"""
    level = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Level"""
    name = Column(mysql.VARCHAR(64), nullable=False)
    """Name"""
    isgroupleader = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Is Group Leader: 0 = False, 1 = True"""
    israidleader = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Is Raid Leader: 0 = False, 1 = True"""
    islooter = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Is Looter: 0 = False, 1 = True"""
