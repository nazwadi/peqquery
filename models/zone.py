from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from meta import mapper_registry

from .graveyards import Graveyard
from .rules import RuleSets


@mapper_registry.mapped
class Launcher:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/launcher/#schema
    """
    __tablename__ = "launcher"
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    """Name"""
    dynamics = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Dynamics"""


@mapper_registry.mapped
class LauncherZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/launcher_zones/#schema
    """
    __tablename__ = "launcher_zones"
    launcher = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    """Launcher"""
    zone = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    port = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=0)
    """Port"""


@mapper_registry.mapped
class ZoneFlags:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone_flags/#schema
    """
    __tablename__ = "zone_flags"
    charID = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    """Unique Character Identifier (see https://docs.eqemu.io/schema/characters/character_data)"""
    zoneID = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""


@mapper_registry.mapped
class Zone:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone/
    """
    __tablename__ = "zone"
    short_name = Column(mysql.VARCHAR(32), nullable=True, primary_key=True, unique=False, default=None)
    """Short Name"""
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Entry Identifier"""
    file_name = Column(mysql.VARCHAR(16), nullable=True, default=None)
    """File Name"""
    long_name = Column(mysql.TEXT, nullable=False, default=None)
    """Long Name"""
    map_file_name = Column(mysql.VARCHAR(100), nullable=True, default=None)
    """Map File Name"""
    safe_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Safe X Coordinate"""
    safe_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Safe Y Coordinate"""
    safe_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Safe Z Coordinate"""
    safe_heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Safe Heading Coordinate"""
    graveyard_id = Column(mysql.FLOAT, ForeignKey(Graveyard.id), nullable=False, default=0)
    """Graveyard Identifier (see https://docs.eqemu.io/schema/graveyards/graveyard/)"""
    min_level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Minimum Level"""
    min_status = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Minimum Status (see https://docs.eqemu.io/server/player/status-levels)"""
    zoneidnumber = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, unique=False, default=0)
    """Unique Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Version"""
    timezone = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    """Timezone"""
    maxclients = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    """Maximum Clients"""
    ruleset = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(RuleSets.ruleset_id),
                     nullable=False, default=0)
    """Ruleset Identifier (see https://docs.eqemu.io/schema/rules/rule_sets/)"""
    note = Column(mysql.VARCHAR(80), nullable=True, default=None)
    """Note"""
    underworld = Column(mysql.FLOAT, nullable=False, default=0)
    """Bottom Z to represent when the player is under the world"""
    minclip = Column(mysql.FLOAT, nullable=False, default=450)
    """Minimum Clipping Distance"""
    maxclip = Column(mysql.FLOAT, nullable=False, default=450)
    """Maximum Clipping Distance"""
    fog_minclip = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Minimum Clipping Distance"""
    fog_maxclip = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Maximum Clipping Distance"""
    fog_blue = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Blue Level: 0 = None, 255 = Max"""
    fog_red = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Red Level: 0 = None, 255 = Max"""
    fog_green = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Green Level: 0 = None, 255 = Max"""
    sky = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """Sky type the client will present as the backdrop"""
    ztype = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """This field is sent directly to the client on zone-in, most zones are set to 0, 1 or 255"""
    zone_exp_multiplier = Column(mysql.DECIMAL(6, 2), nullable=False, default=0.00)
    """This will multiply the XP to this percentage value (decimal based, 100% = 1.0)"""
    walkspeed = Column(mysql.FLOAT, nullable=False, default=0.4)
    """Walkspeed in this zone"""
    time_type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=2)
    """
    This value varies depending on the zone but it is sent to the client on zone in. Most starting zones/newbie areas
    have this value set to 2, dungeons tyically have this set to 0, some zones break from the norm and have values 
    greater than 2, (akanon = 3, blackburrow = 5, cazicthule = 5, crushbone = 5, erudnint = 4, kaladima = 3, etc.)
    """
    fog_red1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Red Level 1: 0 = None, 255 = Max"""
    fog_green1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Green Level 1: 0 = None, 255 = Max"""
    fog_blue1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Blue Level 1: 0 = None, 255 = Max"""
    fog_minclip1 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Minimum Clipping Distance 1"""
    fog_maxclip1 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Maximum Clipping Distance 1"""
    fog_red2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Red Level 2: 0 = None, 255 = Max"""
    fog_green2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Green Level 2: 0 = None, 255 = Max"""
    fog_blue2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Blue Level 2: 0 = None, 255 = Max"""
    fog_minclip2 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Minimum Clipping Distance 2"""
    fog_maxclip2 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Maximum Clipping Distance 2"""
    fog_red3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Red Level 3: 0 = None, 255 = Max"""
    fog_green3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Green Level 3: 0 = None, 255 = Max"""
    fog_blue3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Blue Level 3: 0 = None, 255 = Max"""
    fog_minclip3 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Minimum Clipping Distance 3"""
    fog_maxclip3 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Maximum Clipping Distance 4"""
    fog_red4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Red Level 4: 0 = None, 255 = Max"""
    fog_green4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Green Level 4: 0 = None, 255 = Max"""
    fog_blue4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Fog Blue Level 4: 0 = None, 255 = Max"""
    fog_minclip4 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Minimum Clipping Distance 4"""
    fog_maxclip4 = Column(mysql.FLOAT, nullable=False, default=450)
    """Fog Maximum Clipping Distance 4"""
    fog_density = Column(mysql.FLOAT, nullable=False, default=0)
    """This is the intensity of the fog, this should be a number between 0-1, most commonly used is .1 or .33"""
    flag_needed = Column(mysql.VARCHAR(128), nullable=False)
    """Flag Required (see https://docs.eqemu.io/schema/zone/zone_flags/)"""
    canbind = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """Can Bind: 0 = False, 1 = True (for Caster), 2 = True (for All)"""
    cancombat = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """Can Combat: 0 = False, 1 = True"""
    canlevitate = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """Can Levitate: 0 = False, 1 = True (Does not affect those with #gm on)"""
    castoutdoor = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """Cast Outdoors: 0 = False, 1 = True"""
    hotzone = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Hotzone: 0 = False, 1 = True"""
    insttype = Column(mysql.TINYINT(display_width=1, unsigned=True, zerofill=True), nullable=False, default=0)
    """Instance Type"""
    shutdowndelay = Column(mysql.BIGINT(display_width=16, unsigned=True), nullable=False, default=5000)
    """Shutdown Delay"""
    peqzone = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    """#peqzone: 0 = False, 1 = True"""
    expansion = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    """Expansion (see https://docs.eqemu.io/server/operation/expansion-list)"""
    suspendbuffs = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    """Suspend Buffs: 0 = False, 1 = True"""
    rain_chance1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Chance 1"""
    rain_chance2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Chance 2"""
    rain_chance3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Chance 3"""
    rain_chance4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Chance 4"""
    rain_duration1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Duration 1"""
    rain_duration2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Duration 2"""
    rain_duration3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Duration 3"""
    rain_duration4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Rain Duration 4"""
    snow_chance1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Chance 1"""
    snow_chance2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Chance 2"""
    snow_chance3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Chance 3"""
    snow_chance4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Chance 4"""
    snow_duration1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Duration 1"""
    snow_duration2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Duration 2"""
    snow_duration3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Duration 3"""
    snow_duration4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Snow Duration 4"""
    gravity = Column(mysql.FLOAT, nullable=False, default=0.4)
    """Gravity"""
    type = Column(mysql.INTEGER(display_width=3), nullable=False, default=0)
    """Type (0 = Unknown, 1 = Regular, 2 = Instanced, 3 = Hybrid, 4 = Raid, 5 = City)"""
    skylock = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Sky Lock"""
    fast_regen_hp = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    """Fast Regen Health"""
    fast_regen_mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    """Fast Regen Mana"""
    fast_regen_endurance = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    """Fast Regen Endurance"""
    npc_max_aggro_dist = Column(mysql.INTEGER(display_width=11), nullable=False, default=600)
    """NPC Max Aggro Distance"""
    max_movement_update_range = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=600)
    """Max Movement Update Range"""
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)
    underworld_teleport_index = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    lava_damage = Column(mysql.INTEGER(display_width=11), nullable=True, default=50)
    min_laval_damage = Column(mysql.INTEGER(display_width=11), nullable=False, default=10)


@mapper_registry.mapped
class ZonePoints:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone_points/
    """
    __tablename__ = "zone_points"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Zone Point Identifier"""
    zone = Column(mysql.VARCHAR(32), nullable=True, default=None)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    version = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Version"""
    number = Column(mysql.SMALLINT(display_width=4, unsigned=True), primary_key=True, unique=False, default=1)
    """Represents the iterator field sent in the struct ZonePoint_Entry, zone points for the current zone are sent when
     client zones in (during Client::Handle_Connect_OP_ReqClientSpawn in client_packet.cpp). This number field must be
      unique and also could have a hardcoded equivalent in the client, eg. client is expecting a specific number value
       for a zone point or teleport/object pad, such as in Erudin (erudnext).
       """
    y = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Coordinate"""
    x = Column(mysql.FLOAT, nullable=False, default=0)
    """X Coordinate"""
    z = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Coordinate"""
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Heading Coordinate"""
    target_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Target Y Coordinate"""
    target_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Target X Coordinate"""
    target_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Target Z Coordinate"""
    target_heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Target Heading Coordinate"""
    zoneinst = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=True, default=0)
    """Instance Identifier (see https://docs.eqemu.io/server/instances/instance_list)"""
    target_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                            primary_key=True, unique=True, default=0)
    """Target Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    target_instance = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Target Instance Identifier"""
    buffer = Column(mysql.FLOAT, nullable=True, default=0)
    """Zone Point Buffer"""
    client_version_mask = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=4294967295)
    """Client Version Mask (see https://docs.eqemu.io/server/player/client-version-bitmasks)"""
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)
    is_virtual = Column(mysql.TINYINT(display_width=4), nullable=True, default=0)
    height = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    width = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
