from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from meta import mapper_registry


@mapper_registry.mapped
class InstanceList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/instances/instance_list/
    """
    __tablename__ = "instance_list"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Instance Identifier"""
    zone = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey("Zone.zoneidnumber"),
                  nullable=False, default=0)
    """Zone Identifier"""
    version = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    """Version"""
    is_global = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Is Global: 0 = False, 1 = True"""
    start_time = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Start Time UNIX Timestamp"""
    duration = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Duration in Seconds"""
    never_expires = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Never Expires: 0 = False, 1 = True"""

    instance_list_player = relationship("InstanceListPlayer")
    """Relationship Type: Has-Many, Local Key: id, Relates to Table: instance_list_player, Foreign Key: id"""
#    zone_relationship = relationship("Zone")


@mapper_registry.mapped
class InstanceListPlayer:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/instances/instance_list_player/
    """
    __tablename__ = "instance_list_player"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(InstanceList.id),
                nullable=False, primary_key=True, default=0)
    """Instance Identifier (see https://docs.eqemu.io/schema/instances/instance_list/)"""
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey("CharacterData.id"),
                    nullable=False, primary_key=True, default=0)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""

