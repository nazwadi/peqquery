from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Graveyard:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/graveyards/graveyard/
    """
    __tablename__ = "graveyard"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    zone_id = Column(mysql.INTEGER(display_width=4), nullable=False, unique=False, primary_key=True, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
