from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry


@mapper_registry.mapped
class RespawnTimes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/respawn_times/
    """
    __tablename__ = "respawn_times"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    """Unique Respawn Time Identifier"""
    start = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Start UNIX Timestamp"""
    duration = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Duration in Seconds"""
    instance_id = Column(mysql.SMALLINT(display_width=6), nullable=False, primary_key=True, default=0)
    """Instance Identifier (see https://docs.eqemu.io/schema/instances/instance_list/)"""


@mapper_registry.mapped
class Spawn2:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawn2/
    """
    __tablename__ = "spawn2"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Spawn2 Entry Identifier"""
    spawngroupID = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    """Unique Spawngroup Identifier (see https://docs.eqemu.io/schema/spawns/spawngroup/)"""
    zone = Column(mysql.VARCHAR(32), nullable=True, unique=False, primary_key=True, default=None)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.SMALLINT(5), nullable=False, default=0)
    """Version"""
    x = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    """X Coordinate"""
    y = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    """Y Coordinate"""
    z = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    """Z Coordinate"""
    heading = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    """Heading Coordinate"""
    respawntime = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Respawn Time in Seconds"""
    variance = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Variance in Seconds"""
    pathgrid = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Path Grid Identifier (see https://docs.eqemu.io/schema/grids/grid/)"""
    path_when_zone_idle = Column(mysql.TINYINT(1), nullable=False, default=0)
    _condition = Column(mysql.MEDIUMINT(8, unsigned=True), nullable=False, default=0)
    """Condition"""
    cond_value = Column(mysql.MEDIUMINT(9), nullable=False, default=1)
    """Condition Value"""
    enabled = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """Enabled: 0 = False, 1 = True"""
    animation = Column(mysql.TINYINT(3, unsigned=True), nullable=False, default=0)
    """Animation (see https://docs.eqemu.io/server/npc/npc-animation-types)"""
    min_expansion = Column(mysql.TINYINT(4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    spawngroup = relationship("SpawnGroup", back_populates="spawn2", uselist=False)
    """Relationship Type: One-to-One, Local Key: spawngroupID, Relates to Table: spawngroup, Foreign Key: id"""
    # spawn_entries = relationship("SpawnEntry", foreign_keys="Spawn2.spawngroupID")
    """Relationship Type: Has-Many, Local Key: spawngroupID, Relates to Table: spawnentry, Foreign Key: spawngroupID"""


@mapper_registry.mapped
class SpawnGroup:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawngroup/
    """
    __tablename__ = "spawngroup"
    id = Column(mysql.INTEGER(display_width=11), ForeignKey(Spawn2.spawngroupID), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique Spawn Group Identifier"""
    name = Column(mysql.VARCHAR(50), nullable=False, unique=True)
    """Name"""
    spawn_limit = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Spawn Limit"""
    dist = Column(mysql.FLOAT, nullable=False, default=0)
    """Distance"""
    max_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Max X Coordinate"""
    min_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Min X Coordinate"""
    max_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Max Y Coordinate"""
    min_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Min Y Coordinate"""
    delay = Column(mysql.INTEGER(display_width=11), nullable=False, default=45000)
    """Roaming Delay"""
    mindelay = Column(mysql.INTEGER(display_width=11), nullable=False, default=15000)
    """Minimum Delay"""
    despawn = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    """Despawn Type (see https://docs.eqemu.io/server/npc/spawns/npc-despawn-types)"""
    despawn_timer = Column(mysql.TINYINT(display_width=11), nullable=False, default=100)
    """Despawn Timer in Seconds"""
    wp_spawns = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)

    spawn2 = relationship("Spawn2", back_populates="spawngroup", uselist=False)
    """Relationship Type: One-to-One, Local Key: id, Relates to Table: spawn2, Foreign Key: spawngroupID"""


@mapper_registry.mapped
class SpawnEntry:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawnentry/
    """
    __tablename__ = "spawnentry"
    spawngroupID = Column(mysql.INTEGER(display_width=11), ForeignKey(SpawnGroup.id), nullable=False,
                          primary_key=True, default=0)
    """Unique Spawn Group Identifier (see https://docs.eqemu.io/schema/spawns/spawngroup/)"""
    npcID = Column(mysql.INTEGER(display_width=11), ForeignKey("npc_types.id"),
                   nullable=False, primary_key=True, default=0)
    """NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/)"""
    chance = Column(mysql.SMALLINT(4), nullable=False, default=0)
    """Chance: 0 = Never, 100 = Always"""
    condition_value_filter = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=1)
    min_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    max_expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)

    spawngroup = relationship("SpawnGroup", uselist=False)
    """Relationship Type: One-to-One, Local Key: spawngroupID, Relates to Table: spawngroup, Foreign Key: id"""
    npc_types = relationship("NPCTypes", foreign_keys=[npcID], uselist=False)
    """Relationship Type: One-to-One, Local Key: npcID, Relates to Table: npc_types, Foreign Key: id"""


@mapper_registry.mapped
class SpawnConditions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawn_conditions/
    """
    __tablename__ = "spawn_conditions"
    zone = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    id = Column(mysql.MEDIUMINT(8, unsigned=True), nullable=False, primary_key=True, default=1)
    """Spawn Condition Identifier"""
    value = Column(mysql.MEDIUMINT(9), nullable=False, default=0)
    """Value"""
    onchange = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """On Change Type (see https://docs.eqemu.io/server/npc/spawns/on-change-types)"""
    name = Column(mysql.VARCHAR(255), nullable=False)
    """Name"""


@mapper_registry.mapped
class SpawnConditionValues:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawn_condition_values/
    """
    __tablename__ = "spawn_condition_values"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    """Spawn Condition Identifier (see https://docs.eqemu.io/schema/spawns/spawn_conditions/)"""
    value = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=True, default=None)
    """Value"""
    zone = Column(mysql.VARCHAR(64), nullable=False, primary_key=True, default=None)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    instance_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    """Instance Identifier (see https://docs.eqemu.io/schema/instances/instance_list/)"""


@mapper_registry.mapped
class SpawnEvents:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spawns/spawn_events/
    """
    __tablename__ = "spawn_events"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique Spawn Event Entry Identifier"""
    zone = Column(mysql.VARCHAR(32), nullable=True, default=None)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    cond_id = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    """Spawn Condition Identifier (see https://docs.eqemu.io/schema/spawns/spawn_conditions/)"""
    name = Column(mysql.VARCHAR(255), nullable=False)
    """Name"""
    period = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Period"""
    next_minute = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Next Minute"""
    next_hour = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Next Hour"""
    next_day = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Next Day"""
    next_month = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Next Month"""
    next_year = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Next Year"""
    enabled = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """Enabled: 0 = False, 1 = True"""
    action = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Action Type (see https://docs.eqemu.io/server/npc/spawns/action-types)"""
    argument = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=0)
    """Argument: (Based on Action) 0 = Argument Value"""
    strict = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Strict Date Criteria: 0 = False, 1 = True"""
