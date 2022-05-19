from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from meta import mapper_registry

from .zone import Zone
from .items import Items


@mapper_registry.mapped
class Object:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/objects/object/
    """
    __tablename__ = "object"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Object Identifier"""
    zoneid = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Zone.zoneidnumber),
                    nullable=False, unique=False, primary_key=True, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Version: -1 For All"""
    xpos = Column(mysql.FLOAT, nullable=False, default=0)
    """X Coordinate"""
    ypos = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Coordinate"""
    zpos = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Coordinate"""
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Heading Coordiante"""
    itemid = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                    nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Charges"""
    objectname = Column(mysql.VARCHAR(32), nullable=True, default=None)
    """Object Name"""
    type = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Type (see https://docs.eqemu.io/server/zones/object-types)"""
    icon = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Icon"""
    unknown08 = Column(mysql.MEDIUMINT(display_width=5), nullable=False, default=0)
    """Unknown"""
    unknown10 = Column(mysql.MEDIUMINT(display_width=5), nullable=False, default=0)
    """Unknown"""
    unknown20 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown24 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown60 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown64 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown68 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown72 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown76 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    unknown84 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unknown"""
    size = Column(mysql.FLOAT, nullable=False, default=100)
    """Size"""
    tilt_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Tilt X"""
    tilt_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Tilt Y"""
    display_name = Column(mysql.VARCHAR(64), nullable=True, default=None)
    """Display Name"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    zone = relationship("Zone")
    items = relationship("Items")


@mapper_registry.mapped
class ObjectContents:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/objects/object_contents/
    """
    __tablename__ = "object_contents"
    zoneid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    parentid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    bagidx = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    charges = Column(mysql.SMALLINT(display_width=3), nullable=False, default=0)
    droptime = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
