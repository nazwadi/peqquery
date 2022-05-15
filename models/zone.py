from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class Launcher:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/launcher/#schema
    """
    __tablename__ = "launcher"
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    dynamics = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class LauncherZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/launcher_zones/#schema
    """
    __tablename__ = "launcher_zones"
    launcher = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    zone = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)  # zone shortname
    port = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=0)


@mapper_registry.mapped
class ZoneFlags:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone_flags/#schema
    """
    __tablename__ = "zone_flags"
    charID = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    zoneID = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)


@mapper_registry.mapped
class Zone:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone/
    """
    __tablename__ = "zone"
    short_name = Column(mysql.VARCHAR(32), nullable=True, primary_key=True, unique=False, default=None)
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None, autoincrement="auto")
    file_name = Column(mysql.VARCHAR(16), nullable=True, default=None)
    long_name = Column(mysql.TEXT, nullable=False, default=None)
    map_file_name = Column(mysql.VARCHAR(100), nullable=True, default=None)
    safe_x = Column(mysql.FLOAT, nullable=False, default=0)
    safe_y = Column(mysql.FLOAT, nullable=False, default=0)
    safe_z = Column(mysql.FLOAT, nullable=False, default=0)
    graveyard_id = Column(mysql.FLOAT, nullable=False, default=0)
    min_level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    min_status = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    zoneidnumber = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, unique=False, default=0)
    version = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    timezone = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    maxclients = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    ruleset = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    note = Column(mysql.VARCHAR(80), nullable=True, default=None)
    underworld = Column(mysql.FLOAT, nullable=False, default=0)
    minclip = Column(mysql.FLOAT, nullable=False, default=450)
    maxclip = Column(mysql.FLOAT, nullable=False, default=450)
    fog_minclip = Column(mysql.FLOAT, nullable=False, default=450)
    fog_maxclip = Column(mysql.FLOAT, nullable=False, default=450)
    fog_blue = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_red = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_green = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    sky = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    ztype = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    zone_exp_multiplier = Column(mysql.DECIMAL(6, 2), nullable=False, default=0.00)
    walkspeed = Column(mysql.FLOAT, nullable=False, default=0.4)
    time_type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=2)
    fog_red1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_green1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_blue1 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_minclip1 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_maxclip1 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_red2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_green2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_blue2 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_minclip2 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_maxclip2 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_red3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_green3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_blue3 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_minclip3 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_maxclip3 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_red4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_green4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_blue4 = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    fog_minclip4 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_maxclip4 = Column(mysql.FLOAT, nullable=False, default=450)
    fog_density = Column(mysql.FLOAT, nullable=False, default=0)
    flag_needed = Column(mysql.VARCHAR(128), nullable=False)
    canbind = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    cancombat = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    canlevitate = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    castoutdoor = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    hotzone = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    insttype = Column(mysql.TINYINT(display_width=1, unsigned=True, zerofill=True), nullable=False, default=0)
    shutdowndelay = Column(mysql.BIGINT(display_width=16, unsigned=True), nullable=False, default=5000)
    peqzone = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    expansion = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    suspendbuffs = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    rain_chance1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_chance2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_chance3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_chance4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_duration1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_duration2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_duration3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    rain_duration4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_chance1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_chance2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_chance3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_chance4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_duration1 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_duration2 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_duration3 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    snow_duration4 = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    gravity = Column(mysql.FLOAT, nullable=False, default=0.4)
    type = Column(mysql.INTEGER(display_width=3), nullable=False, default=0)
    skylock = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    fast_regen_hp = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    fast_regen_mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    fast_regen_endurance = Column(mysql.INTEGER(display_width=11), nullable=False, default=180)
    npc_max_aggro_dist = Column(mysql.INTEGER(display_width=11), nullable=False, default=600)
    max_movement_update_range = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=600)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)
    underworld_teleport_index = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)


@mapper_registry.mapped
class ZonePoints:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/zone/zone_points/
    """
    __tablename__ = "zone_points"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    zone = Column(mysql.VARCHAR(32), nullable=True, default=None)
    version = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    number = Column(mysql.SMALLINT(display_width=4, unsigned=True), primary_key=True, unique=False, default=1)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    target_y = Column(mysql.FLOAT, nullable=False, default=0)
    target_x = Column(mysql.FLOAT, nullable=False, default=0)
    target_z = Column(mysql.FLOAT, nullable=False, default=0)
    target_heading = Column(mysql.FLOAT, nullable=False, default=0)
    zoneinst = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=True, default=0)
    target_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                            primary_key=True, unique=True, default=0)
    target_instance = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    buffer = Column(mysql.FLOAT, nullable=True, default=0)
    client_version_mask = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=4294967295)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True, default=None)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True, default=None)
    is_virtual = Column(mysql.TINYINT(display_width=4), nullable=True, default=0)
    height = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    width = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
