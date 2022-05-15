from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import mysql

from meta import mapper_registry
from .account import Account
from .items import Items


@mapper_registry.mapped
class BannedIPs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/banned_ips/
    """
    __tablename__ = "banned_ips"
    ip_address = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    notes = Column(mysql.VARCHAR(32), nullable=True)


@mapper_registry.mapped
class BugReports:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/bug_reports/
    """
    __tablename__ = "bug_reports"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, primary_key=True, autoincrement="auto")
    """Unique Bug Report Identifier"""
    zone = Column(mysql.VARCHAR(32), nullable=True, default="Unknown")
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    client_version_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Client Version Identifier (see https://docs.eqemu.io/server/player/client-version-bitmasks)"""
    client_version_name = Column(mysql.VARCHAR(24), nullable=False, default="Unknown")
    """Client Version Name (see https://docs.eqemu.io/server/player/client-version-bitmasks)"""
    account_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Account.id),
                        nullable=False, default=0)
    """Account Identifier (see https://docs.eqemu.io/schema/account/account/)"""
    character_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    character_name = Column(mysql.VARCHAR(64), nullable=False, default="Unknown")
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    reporter_spoof = Column(mysql.TINYINT(1), nullable=False, default=1)
    """Reporter Spoof"""
    category_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Category Identifier"""
    category_name = Column(mysql.VARCHAR(64), nullable=False, default="Other")
    """Category Name"""
    reporter_name = Column(mysql.VARCHAR(64), nullable=False, default="Unknown")
    """Reporter Name"""
    ui_path = Column(mysql.VARCHAR(128), nullable=False, default="Unknown")
    """UI Path"""
    pos_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Position X Coordinate"""
    pos_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Position Y Coordinate"""
    pos_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Position Z Coordinate"""
    heading = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Heading Coordinate"""
    time_played = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Time Played in Seconds"""
    target_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Target Identifier"""
    target_name = Column(mysql.VARCHAR(64), nullable=False, default="Unknown")
    """Target Name"""
    optional_info_mask = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Optional Info Mask: 0 = False, 1 = True"""
    _can_duplicate = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Can Duplicate: 0 = False, 1 = True"""
    _crash_bug = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Crash Bug"""
    _target_info = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Target Info"""
    _character_flags = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Character Flags"""
    _unknown_value = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """Unknown"""
    bug_report = Column(mysql.VARCHAR(1024), nullable=False)
    """Bug Report"""
    system_info = Column(mysql.VARCHAR(1024), nullable=False)
    """System Information"""
    report_datetime = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP")
    """Report Datetime"""
    bug_status = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Bug Status"""
    last_review = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    """Last Review Datetime"""
    last_reviewer = Column(mysql.VARCHAR(64), nullable=False, default="None")
    """Last Reviewer"""
    reviewer_notes = Column(mysql.VARCHAR(1024), nullable=False)
    """Reviewer Notes"""

    account = relationship("Account", back_populates="bug_reports")


@mapper_registry.mapped
class Bugs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/bugs/
    """
    __tablename__ = "bugs"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    zone = Column(mysql.VARCHAR(32), nullable=False)
    name = Column(mysql.VARCHAR(64), nullable=False)
    ui = Column(mysql.VARCHAR(128), nullable=False)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    type = Column(mysql.VARCHAR(64), nullable=False)
    flag = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False)
    target = Column(mysql.VARCHAR(64), nullable=True)
    bug = Column(mysql.VARCHAR(1024), nullable=False)
    date = Column(mysql.DATE, nullable=False)
    status = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class ChatChannels:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/chatchannels/
    """
    __tablename__ = "chat_channels"
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    owner = Column(mysql.VARCHAR(64), nullable=False)
    password = Column(mysql.VARCHAR(64), nullable=False)
    minstatus = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)


@mapper_registry.mapped
class CommandSettings:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/command_settings/
    """
    __tablename__ = "command_settings"
    command = Column(mysql.VARCHAR(128), nullable=False, primary_key=True)
    access = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    aliases = Column(mysql.VARCHAR(256), nullable=False)


@mapper_registry.mapped
class DBVersion:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/db_version/
    """
    __tablename__ = "db_version"
    version = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=True, default=0)
    """Primary Key is not actually defined in SQL"""


@mapper_registry.mapped
class DiscoveredItems:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/discovered_items/
    """
    __tablename__ = "discovered_items"
    item_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Items.id), primary_key=True,
                     nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    char_name = Column(mysql.VARCHAR(64), nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    discovered_date = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Discovered Date UNIX Timestamp"""
    account_status = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Account Status (see https://docs.eqemu.io/server/player/status-levels)"""


@mapper_registry.mapped
class EQTime:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/eqtime/
    """
    __tablename__ = "eqtime"
    minute = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""
    hour = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""
    day = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""
    month = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""
    year = Column(mysql.INTEGER(display_width=4), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""
    realtime = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in SQL"""


@mapper_registry.mapped
class EventLog:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/eventlog/
    """
    __tablename__ = "eventlog"
    id = Column(mysql.INTEGER(10, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    accoountname = Column(mysql.VARCHAR(30), nullable=False)
    accountid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=True, default=0)
    status = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    charname = Column(mysql.VARCHAR(64), nullable=False)
    target = Column(mysql.VARCHAR(64), nullable=True, default="None")
    time = Column(mysql.TIMESTAMP, nullable=False, default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    descriptiontype = Column(mysql.TEXT, nullable=False)
    event_nid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class GMIPs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/gm_ips/
    """
    __tablename__ = "gm_ips"
    name = Column(mysql.VARCHAR(64), nullable=False)
    account_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True)
    ip_address = Column(mysql.VARCHAR(15), nullable=False, primary_key=True)


@mapper_registry.mapped
class Hackers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/hackers/
    """
    __tablename__ = "hackers"
    id = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, autoincrement="auto")
    account = Column(mysql.TEXT, nullable=False)
    name = Column(mysql.TEXT, nullable=False)
    hacked = Column(mysql.TEXT, nullable=False)
    zone = Column(mysql.TEXT, nullable=True)
    date = Column(mysql.TIMESTAMP, nullable=False, default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


@mapper_registry.mapped
class IPExemptions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/ip_exemptions/
    """
    __tablename__ = "ip_exemptions"
    exemption_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    exemption_ip = Column(mysql.VARCHAR(255), nullable=True)
    exemption_amount = Column(mysql.INTEGER(display_width=11), nullable=True)


@mapper_registry.mapped
class LevelExpMods:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/level_exp_mods/
    """
    __tablename__ = "level_exp_mods"
    level = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    exp_mod = Column(mysql.FLOAT, nullable=True)     # Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%
    aa_exp_mod = Column(mysql.FLOAT, nullable=True)  # AA Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%


@mapper_registry.mapped
class LogSysCategories:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/logsys_categories/
    """
    __tablename__ = "logsys_categories"
    log_category_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    log_category_description = Column(mysql.VARCHAR(150), nullable=True)
    log_to_console = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)  # 0 = False, 1 = True
    log_to_file = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)     # 0 = False, 1 = True
    log_to_gmsay = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)    # 0 = False, 1 = True


@mapper_registry.mapped
class NameFilter:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/name_filter/
    """
    __tablename__ = "name_filter"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    name = Column(mysql.VARCHAR(30), nullable=False, index=True)  # index=True should set Key column to "MUL"


@mapper_registry.mapped
class PerlEventExportSettings:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/perl_event_export_settings/
    """
    __tablename__ = "perl_event_export_settings"
    event_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True)
    event_description = Column(mysql.VARCHAR(150), nullable=True)
    export_qglobals = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)  # 0 = False, 1 = True
    export_mob = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)       # 0 = False, 1 = True
    export_zone = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)      # 0 = False, 1 = True
    export_item = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)      # 0 = False, 1 = True
    export_event = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)     # 0 = False, 1 = True


@mapper_registry.mapped
class Petitions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/petitions/
    """
    __tablename__ = "petitions"
    dib = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    petid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, index=True, default=0)
    charname = Column(mysql.VARCHAR(32), nullable=False)
    accountname = Column(mysql.VARCHAR(32), nullable=False)
    lastgm = Column(mysql.VARCHAR(32), nullable=False)
    petitiontext = Column(mysql.TEXT, nullable=False)
    gmtext = Column(mysql.TEXT, nullable=True)
    zone = Column(mysql.VARCHAR(32), nullable=False)
    urgency = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    charclass = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    charrace = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    charlevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    checkouts = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unavailables = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ischeckedout = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    senttime = Column(mysql.BIGINT(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class ProfanityList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/profanity_list/
    """
    __tablename__ = "profanity_list"
    word = Column(mysql.VARCHAR(16), primary_key=True, nullable=False)
    """Primary Key is not actually defined in SQL"""


@mapper_registry.mapped
class Reports:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/reports/
    """
    __tablename__ = "reports"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, autoincrement="auto")
    name = Column(mysql.VARCHAR(64), nullable=True)
    reported = Column(mysql.VARCHAR(64), nullable=True)
    reported_text = Column(mysql.TEXT, nullable=True)


@mapper_registry.mapped
class SayLink:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/saylink/
    """
    __tablename__ = "saylink"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, autoincrement="auto")
    phrase = Column(mysql.VARCHAR(64), nullable=False, index=True)


@mapper_registry.mapped
class StartZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/start_zones/
    """
    __tablename__ = "start_zones"
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    zone_id = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    bind_id = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    player_choice = Column(mysql.INTEGER(display_width=2), nullable=False, primary_key=True, default=0)
    player_class = Column(mysql.INTEGER(display_width=2), nullable=False, primary_key=True, default=0)
    player_deity = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    player_race = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    start_zone = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    bind_x = Column(mysql.FLOAT, nullable=False, default=0)
    bind_y = Column(mysql.FLOAT, nullable=False, default=0)
    bind_z = Column(mysql.FLOAT, nullable=False, default=0)
    select_rank = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=50)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)


@mapper_registry.mapped
class StartingItems:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/starting_items/

    Relationships:
        | Relationship Type | Local Key   | Relates to Table  | Foreign Key |
        | ----------------- | ---------   | ----------------  | ----------- |
        | One-to-One        | zone_id     | zone              | zoneidnumber|
        | One-to-One        | itemid      | items             | id          |
    """
    __tablename__ = "starting_items"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    race = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)  # Race: 0 = All
    _class = Column("class", mysql.INTEGER(display_width=11), nullable=False, default=0)  # Class: 0 = All
    deityid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)  # Deity: 0 = All
    zoneid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)  # Zone Identifier ("zone.id")
    itemid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)  # Item Identifier ("items.id")
    item_charges = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    gm = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)  # GM: 0 = False, 1 = True
    slot = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=-1)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)


@mapper_registry.mapped
class Variables:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/variables/
    """
    __tablename__ = "variables"
    varname = Column(mysql.VARCHAR(35), nullable=False, primary_key=True)
    value = Column(mysql.TEXT, nullable=False)
    information = Column(mysql.TEXT, nullable=False)
    ts = Column(mysql.TIMESTAMP, nullable=False, default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


@mapper_registry.mapped
class VeteranRewardTemplates:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/veteran_reward_templates/
    """
    __tablename__ = "veteran_reward_templates"
    claim_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    name = Column(mysql.VARCHAR(64), nullable=False)
    item_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False)  # Item identifier: "items.id"
    charges = Column(mysql.SMALLINT(display_width=5, unsigned=True))
    reward_slot = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True)
