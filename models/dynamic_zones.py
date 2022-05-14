from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class DynamicZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/dynamic-zones/dynamic_zones/
    """
    __tablename__ = "dynamic_zones"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    instance_id = Column(mysql.INTEGER(display_width=10), nullable=False, unique=True, default=0)
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    uuid = Column(mysql.VARCHAR(36), nullable=False, default=None)
    name = Column(mysql.VARCHAR(128), nullable=False)
    leader_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    min_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    max_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    compass_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    compass_x = Column(mysql.FLOAT, nullable=False, default=0)
    compass_y = Column(mysql.FLOAT, nullable=False, default=0)
    compass_z = Column(mysql.FLOAT, nullable=False, default=0)
    safe_return_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    safe_return_x = Column(mysql.FLOAT, nullable=False, default=0)
    safe_return_y = Column(mysql.FLOAT, nullable=False, default=0)
    safe_return_z = Column(mysql.FLOAT, nullable=False, default=0)
    safe_return_heading = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_x = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_y = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_z = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_heading = Column(mysql.FLOAT, nullable=False, default=0)
    has_zone_in = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class DynamicZoneMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/dynamic-zones/dynamic_zone_members/
    """
    __tablename__ = "dynamic_zone_members"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    dynamic_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                             unique=False, primary_key=True, default=0)
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                          unique=False, primary_key=True, default=0)
