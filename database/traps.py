from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class LDONTrapEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/ldon_trap_entries/
    """
    __tablename__ = "ldon_trap_entries"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    trap_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)


@mapper_registry.mapped
class LDONTrapEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/ldon_trap_entries/
    """
    __tablename__ = "ldon_trap_templates"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    spell_id = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    skill = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    locked = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)  # 0 = False, 1 = True


@mapper_registry.mapped
class Traps:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/traps/
    """
    __tablename__ = "traps"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    zone = Column(mysql.VARCHAR(16), nullable=False, unique=False, primary_key=True)
    version = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    x = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    y = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    z = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    chance = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    maxzdiff = Column(mysql.FLOAT, nullable=False, default=0)
    radius = Column(mysql.FLOAT, nullable=False, default=0)
    effect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effectvalue = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effectvalue2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    message = Column(mysql.VARCHAR(200), nullable=False)
    skill = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    level = Column(mysql.MEDIUMINT(display_width=4, unsigned=True), nullable=False, default=1)
    respawn_time = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=60)
    respawn_var = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    triggered_number = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    group = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    despawn_when_triggered = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    undetectable = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    zone_relationship = relationship("Zone", back_populates="traps")
