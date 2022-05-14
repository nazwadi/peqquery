from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class ContentFlags:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/flagging/content_flags/
    """
    __tablename__ = "content_flags"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    flag_name = Column(mysql.VARCHAR(75), nullable=True, default=None)
    enabled = Column(mysql.TINYINT(4), nullable=True, default=None)
    notes = Column(mysql.TEXT, nullable=True, default=None)
