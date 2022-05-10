from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Object:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/objects/object/
    """
    __tablename__ = "object"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    zoneid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, unique=False, primary_key=True, default=0)
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    xpos = Column(mysql.FLOAT, nullable=False, default=0)
    ypos = Column(mysql.FLOAT, nullable=False, default=0)
    zpos = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    itemid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=False, default=0)
    objectname = Column(mysql.VARCHAR(32), nullable=True, default=None)
    type = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    icon = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown08 = Column(mysql.MEDIUMINT(display_width=5), nullable=False, default=0)
    unknown10 = Column(mysql.MEDIUMINT(display_width=5), nullable=False, default=0)
    unknown20 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown24 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown60 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown64 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown68 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown72 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown76 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unknown84 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    size = Column(mysql.FLOAT, nullable=False, default=100)
    tilt_x = Column(mysql.FLOAT, nullable=False, default=0)
    tilt_y = Column(mysql.FLOAT, nullable=False, default=0)
    display_name = Column(mysql.VARCHAR(64), nullable=True, default=None)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    zone = relationship("Zone", back_populates="object")
    items = relationship("Items", back_populates="object")


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
