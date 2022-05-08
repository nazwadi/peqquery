from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class GroupId:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/groups/group_id/
    """
    __tablename__ = "group_id"
    groupid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=None)
    charid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=None)
    name = Column(mysql.VARCHAR(64), nullable=False, default=None)
    ismerc = Column(mysql.TINYINT(display_width=3), nullable=False, primary_key=True, default=0)  # 0 = False, 1 = True


@mapper_registry.mapped
class GroupLeaders:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/groups/group_leaders/
    """
    __tablename__ = "group_leaders"
    gid = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    leadername = Column(mysql.VARCHAR(64), nullable=False)
    marknpc = Column(mysql.VARCHAR(64), nullable=False)
    leadershipaa = Column(mysql.TINYBLOB, nullable=True, default=None)
    maintank = Column(mysql.VARCHAR(64), nullable=False)
    assist = Column(mysql.VARCHAR(64), nullable=False)
    puller = Column(mysql.VARCHAR(64), nullable=False)
    mentoree = Column(mysql.VARCHAR(64), nullable=False, default=None)
    mentor_percent = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
