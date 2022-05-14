from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Horses:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/horses/horses/#schema
    """
    __tablename__ = "horses"
    filename = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    race = Column(mysql.SMALLINT(display_width=3), nullable=False, default=216)
    gender = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    texture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    mountspeed = Column(mysql.FLOAT(4, 2), nullable=False, default=0.75)
    notes = Column(mysql.VARCHAR(64), nullable=True, default="Notes")
