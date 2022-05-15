from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class AdventureDetails:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_details/
    """
    __tablename__ = "adventure_details"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    type = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    duration = Column(mysql.INTEGER(display_width=11, unsigned=False), nullable=False, default=0)
    duration_code = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    title = Column(mysql.VARCHAR(100), nullable=False)
    description = Column(mysql.TEXT, nullable=False, default=None)
    reward = Column(mysql.VARCHAR(64), nullable=False)
    rewardid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    cashreward = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    xpreward = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    rewardmethod = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=2)
    reward_radiant_crystals = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    reward_ebon_crystals = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    level_spread = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    min_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    max_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    repeatable = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=1)
    faction_reward = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    completion_emote = Column(mysql.VARCHAR(512), nullable=False)
    replay_timer_seconds = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    request_timer_seconds = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class AdventureMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_members/
    """
    __tablename__ = "adventure_members"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                unique=False, primary_key=True, default=None)
    charid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)


@mapper_registry.mapped
class AdventureStats:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_stats/
    """
    __tablename__ = "adventure_stats"
    player_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    guk_wins = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    mir_wins = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    mmc_wins = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    ruj_wins = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    tak_wins = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    guk_losses = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    mir_losses = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    mmc_losses = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    ruj_losses = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    tak_losses = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class AdventureTemplate:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_template/
    """
    __tablename__ = "adventure_template"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    zone = Column(mysql.VARCHAR(64), nullable=False, default=None)
    zone_version = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    is_hard = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    is_raid = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    min_level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    max_level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=65)
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    type_data = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    type_count = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    assa_x = Column(mysql.FLOAT, nullable=False, default=0)
    assa_y = Column(mysql.FLOAT, nullable=False, default=0)
    assa_z = Column(mysql.FLOAT, nullable=False, default=0)
    assa_h = Column(mysql.FLOAT, nullable=False, default=0)
    text = Column(mysql.VARCHAR(511), nullable=True, default=None)
    duration = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=7200)
    zone_in_time = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1800)
    win_points = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    lose_points = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    theme = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    zone_in_zone_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    zone_in_x = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_y = Column(mysql.FLOAT, nullable=False, default=0)
    zone_in_object_id = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    dest_x = Column(mysql.FLOAT, nullable=False, default=0)
    dest_y = Column(mysql.FLOAT, nullable=False, default=0)
    dest_z = Column(mysql.FLOAT, nullable=False, default=0)
    dest_h = Column(mysql.FLOAT, nullable=False, default=0)
    graveyard_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    graveyard_x = Column(mysql.FLOAT, nullable=False, default=0)
    graveyard_y = Column(mysql.FLOAT, nullable=False, default=0)
    graveyard_z = Column(mysql.FLOAT, nullable=False, default=0)
    graveyard_radius = Column(mysql.FLOAT(unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class AdventureTemplateEntry:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_template_entry/
    """
    __tablename__ = "adventure_template_entry"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    template_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)


@mapper_registry.mapped
class AdventureTemplateEntryFlavor:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/adventures/adventure_template_entry_flavor/
    """
    __tablename__ = "adventure_template_entry_flavor"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    text = Column(mysql.VARCHAR(512), nullable=False, default=None)
