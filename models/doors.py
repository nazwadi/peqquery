from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base
from .items import Items


class Doors(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/doors/doors/

    Relationships:
        | Relationship Type | Local Key | Relates to Table  | Foreign Key |
        | ----------------- | --------- | ----------------  | ----------- |
        | One-to-One        | keyitem   | items             | id          |
        | One-to-One        | zone      | zone              | short_name  |
    """
    __tablename__ = "doors"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Entry Identifier"""
    doorid = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Unique Door Identifier"""
    zone = Column(mysql.VARCHAR(32), nullable=True, unique=False, primary_key=True, default=None)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Zone Version: -1 For All"""
    name = Column(mysql.VARCHAR(32), nullable=False)
    """This is the name of the door, such as 'IT11161' or 'POPCREATE501', for names of objects you can see."""
    pos_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Door Y Coordinate"""
    pos_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Door X Coordinate"""
    pos_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Door Z Coordinate"""
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Door Heading Coordinate"""
    opentype = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Door Open Type (see https://docs.eqemu.io/server/zones/door-open-types)"""
    guild = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Guild Identifier (see https://docs.eqemu.io/schema/guilds/guilds/)"""
    lockpick = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Lockpicking Skill Required: -1 = Unpickable"""
    keyitem = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                     nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    nokeyring = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """No Key Ring: 0 = False, 1 = True"""
    triggerdoor = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Trigger Door: 0 For Current Door or use a Unique Door Identifier"""
    triggertype = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Trigger Type: 1 = Open a Type 255 door, 255 = Will Not Open"""
    disable_timer = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    """Disable Timer"""
    doorisopen = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    """Door is Open: 0 = False, 1 = True"""
    door_param = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Door Parameter"""
    dest_zone = Column(mysql.VARCHAR(32), nullable=True, default="NONE")
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    dest_instance = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Destination Instance (see https://docs.eqemu.io/schema/instances/instance_list/)"""
    dest_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Destination X Coordinate"""
    dest_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Destination Y Coordinate"""
    dest_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Destination Z Coordinate"""
    dest_heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Destination Heading Coordinate"""
    invert_state = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """
    This column will basically behave like such: if the door has a click type and it is to raise up like a door, it
    will be raised on spawn of the door. Meaning it is inverted. Another example: If a Door Open Type is set to a 
    spinning object on click, you could set this to 1 to have the door be spinning on spawn.
    """
    incline = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Incline"""
    size = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=100)
    """Size"""
    buffer = Column(mysql.FLOAT, nullable=False, default=100)
    """Unused"""
    client_version_mask = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=4294967295)
    """Client Version Mask (see https://docs.eqemu.io/server/player/client-version-bitmasks)"""
    is_ldon_door = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    """Is LDoN Door: 0 = False, 1 = True"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items = relationship("Items", back_populates="doors", uselist=False)
    """Relationship Type: One-to-One, Local Key: keyitem, Relates to Table: items, Foreign Key: id"""
#    zone = relationship("Zone", uselist=False)
    """Relationship Type: One-to-One, Local Key: zone, Relates to Table: zone, Foreign Key: short_name"""
