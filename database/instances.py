from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class InstanceList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/instances/instance_list/
    """
    __tablename__ = "instance_list"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    zone = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    version = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    is_global = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)  # 0 = False, 1 = True
    start_time = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    duration = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    never_expires = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)

    instance_list_player = relationship("InstanceListPlayer", back_populates="instance_list")
    zone_relationship = relationship("Zone", back_populates="instance_list")


@mapper_registry.mapped
class InstanceListPlayer:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/instances/instance_list_player/
    """
    __tablename__ = "instance_list_player"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)

