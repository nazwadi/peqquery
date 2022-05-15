from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class CharacterExpeditionLockouts:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/expeditions/character_expedition_lockouts/
    """
    __tablename__ = "character_expedition_lockouts"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="true")
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                          unique=False, primary_key=True, default=None)
    expedition_name = Column(mysql.VARCHAR(128), nullable=False, default=None)
    event_name = Column(mysql.VARCHAR(256), nullable=False, default=None)
    expire_time = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP")
    duration = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    from_expedition_uuid = Column(mysql.VARCHAR(36), nullable=False, default=None)


@mapper_registry.mapped
class Expeditions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/expeditions/expeditions/
    """
    __tablename__ = "expeditions"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    dynamic_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, unique=True, default=0)
    add_replay_on_join = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    is_locked = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class ExpeditionLockouts:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/expeditions/expedition_lockouts/
    """
    __tablename__ = "expedition_lockouts"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    expedition_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                           unique=False, primary_key=True, default=None)
    event_name = Column(mysql.VARCHAR(256), nullable=False, default=None)
    expire_time = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP")
    duration = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    from_expedition_uuid = Column(mysql.VARCHAR(36), nullable=False, default=None)
