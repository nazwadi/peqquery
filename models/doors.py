from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Doors:
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
    doorid = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    zone = Column(mysql.VARCHAR(32), nullable=True, unique=False, primary_key=True, default=None)
    version = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    name = Column(mysql.VARCHAR(32), nullable=False)
    pos_y = Column(mysql.FLOAT, nullable=False, default=0)
    pos_x = Column(mysql.FLOAT, nullable=False, default=0)
    pos_z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    opentype = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    guild = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    lockpick = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    keyitem = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    nokeyring = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    triggerdoor = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    triggertype = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    disable_timer = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    doorisopen = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    door_param = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    dest_zone = Column(mysql.VARCHAR(32), nullable=True, default="NONE")
    dest_instance = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    dest_x = Column(mysql.FLOAT, nullable=False, default=0)
    dest_y = Column(mysql.FLOAT, nullable=False, default=0)
    dest_z = Column(mysql.FLOAT, nullable=False, default=0)
    dest_heading = Column(mysql.FLOAT, nullable=False, default=0)
    invert_state = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    incline = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    size = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=100)
    buffer = Column(mysql.FLOAT, nullable=False, default=100)
    client_version_mask = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=4294967295)
    is_ldon_door = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    items_relationship = relationship("Items", back_populates="doors")
    zone_relationship = relationship("Zone", back_populates="doors")
