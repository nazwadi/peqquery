from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import mapper_registry


@mapper_registry.mapped
class Timers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/timers/timers/
    """
    __tablename__ = "timers"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    type = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, primary_key=True, default=0)
    start = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    duration = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    enable = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
