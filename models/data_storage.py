from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import Base


class DataBuckets(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/data-storage/data_buckets/
    """
    __tablename__ = "data_buckets"
    id = Column(mysql.BIGINT(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    key = Column(mysql.VARCHAR(100), nullable=True, unique=False, primary_key=True, default=None)
    value = Column(mysql.TEXT, nullable=True, default=None)
    expires = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)


class QuestGlobals(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/data-storage/quest_globals/
    """
    __tablename__ = "quest_globals"
    charid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    npcid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    zoneid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    name = Column(mysql.VARCHAR(65), nullable=False, primary_key=True)
    value = Column(mysql.VARCHAR(128), nullable=False, default="?")
    expdate = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
