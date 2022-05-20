from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from meta import mapper_registry

from .spells import SpellsNew
from .zone import Zone


@mapper_registry.mapped
class LDONTrapTemplates:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/ldon_trap_entries/
    """
    __tablename__ = "ldon_trap_templates"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    """Unique LDoN Trap Template Identifier"""
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """Trap Type (see https://docs.eqemu.io/server/zones/trap-types)"""
    spell_id = Column(mysql.SMALLINT(display_width=5, unsigned=True), ForeignKey(SpellsNew.id),
                      nullable=False, default=0)
    """Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    skill = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    """Skill (see https://docs.eqemu.io/server/player/skills)"""
    locked = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Locked: 0 = False, 1 = True"""


@mapper_registry.mapped
class LDONTrapEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/ldon_trap_entries/
    """
    __tablename__ = "ldon_trap_entries"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    """Unique LDoN Trap Entry Identifier"""
    trap_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(LDONTrapTemplates.id),
                     nullable=False, primary_key=True, default=0)
    """Trap Identifier (see https://docs.eqemu.io/schema/traps/ldon_trap_templates/)"""


@mapper_registry.mapped
class Traps:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/traps/traps/
    """
    __tablename__ = "traps"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Trap Identifier"""
    zone = Column(mysql.VARCHAR(16), ForeignKey(Zone.short_name), nullable=False, unique=False, primary_key=True)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    """Version: -1 For All"""
    x = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """X Coordinate"""
    y = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Y Coordinate"""
    z = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Z Coordinate"""
    chance = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Chance: 0 = None, 100 = Always"""
    maxzdiff = Column(mysql.FLOAT, nullable=False, default=0)
    """Max Z Difference"""
    radius = Column(mysql.FLOAT, nullable=False, default=0)
    """Trap Radius"""
    effect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Trap Type (see https://docs.eqemu.io/server/zones/trap-types)"""
    effectvalue = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """
    Effect Value: (Based on Trap Type)
        0 = Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/),
        1 = Radius,
        2 = NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/),
        3 = NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/),
        4 = Minimum Damage"""
    effectvalue2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """
    Effect Value 2: (Based on Trap Type) 0 = Unused, 1 = (0 = Everything Will Aggro, 1 = Only KoS Will Agro),
     2 = Number of NPCs, 3 = Number of NPCs, 4 = Maximum Damage"""
    message = Column(mysql.VARCHAR(200), nullable=False)
    """Message"""
    skill = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Skill Required (see https://docs.eqemu.io/server/player/skills)"""
    level = Column(mysql.MEDIUMINT(display_width=4, unsigned=True), nullable=False, default=1)
    """Level"""
    respawn_time = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=60)
    """Respawn Timer in Seconds"""
    respawn_var = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Random Respawn Timer Variance in Seconds"""
    triggered_number = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Triggered Member"""
    group = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Group"""
    despawn_when_triggered = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Despawn When Triggered: 0 = False, 1 = True"""
    undetectable = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Undetectable: 0 = False, 1 = True"""
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    zone_relationship = relationship("Zone")
