from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Grid:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/grids/grid/
    """
    __tablename__ = "grid"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=0)
    zoneid = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=0)
    type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    type2 = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)


@mapper_registry.mapped
class GridEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/grids/grid_entries/
    """
    __tablename__ = "grid_entries"
    gridid = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=0)
    zoneid = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=0)
    number = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    pause = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    centerpoint = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
