from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class GroundSpawns:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/ground-spawns/ground_spawns/
    """
    __tablename__ = "ground_spawns"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    zoneid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                    unique=False, primary_key=True, default=0)
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    max_x = Column(mysql.FLOAT, nullable=False, default=2000)
    max_y = Column(mysql.FLOAT, nullable=False, default=2000)
    max_z = Column(mysql.FLOAT, nullable=False, default=10000)
    min_x = Column(mysql.FLOAT, nullable=False, default=-2000)
    min_y = Column(mysql.FLOAT, nullable=False, default=-2000)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    name = Column(mysql.VARCHAR(16), nullable=False)
    item = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    max_allowed = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    comment = Column(mysql.VARCHAR(255), nullable=False)
    respawn_timer = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=300)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)
