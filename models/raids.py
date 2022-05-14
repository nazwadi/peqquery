from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

from .groups import GroupId

mapper_registry = registry()


@mapper_registry.mapped
class RaidDetails:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/raids/raid_details/
    """
    __tablename__ = "raid_details"
    raidid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    loottype = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    locked = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    motd = Column(mysql.VARCHAR(1024), nullable=True, default=None)

    raid_leaders = relationship("RaidLeaders", back_populates="raid_details")
    raid_members = relationship("RaidMembers", back_populates="raid_details")


@mapper_registry.mapped
class RaidLeaders:
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


@mapper_registry.mapped
class RaidMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/raids/raid_members/
    """
    __tablename__ = "raid_members"
    raidid = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    charid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    groupid = Column(mysql.INTEGER(display_width=4, unsigned=True), nullable=False, default=0)
    _class = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    level = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    name = Column(mysql.VARCHAR(64), nullable=False)
    isgroupleader = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    israidleader = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    islooter = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
