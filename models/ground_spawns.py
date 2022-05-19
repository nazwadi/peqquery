from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .zone import Zone
from .items import Items


@mapper_registry.mapped
class GroundSpawns:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/ground-spawns/ground_spawns/
    """
    __tablename__ = "ground_spawns"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique Ground Spawn Identifier"""
    zoneid = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(Zone.zoneidnumber), nullable=False,
                    unique=False, primary_key=True, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Version: -1 For All"""
    max_x = Column(mysql.FLOAT, nullable=False, default=2000)
    """Maximum X Coordinate"""
    max_y = Column(mysql.FLOAT, nullable=False, default=2000)
    """Maximum Y Coordinate"""
    max_z = Column(mysql.FLOAT, nullable=False, default=10000)
    """Maximum Z Coordinate"""
    min_x = Column(mysql.FLOAT, nullable=False, default=-2000)
    """Minimum X Coordinate"""
    min_y = Column(mysql.FLOAT, nullable=False, default=-2000)
    """Minimum Y Coordinate"""
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Heading Coordinate"""
    name = Column(mysql.VARCHAR(16), nullable=False)
    """Name"""
    item = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(Items.id), nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    max_allowed = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    """Max Allowed"""
    comment = Column(mysql.VARCHAR(255), nullable=False)
    """Comment"""
    respawn_timer = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=300)
    """Respawn Timer in Seconds"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    zone = relationship("Zone")
    """Relationship Type: One-to-One, Local Key: zoneid, Relates to Table: zone, Foreign Key: zoneidnumber"""
    items = relationship("Items", back_populates="ground_spawns")
    """Relationship Type: One-to-One, Local Key: item, Relates to Table: items, Foreign Key: id"""
