from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import mysql

from meta import mapper_registry
from .account import Account
from .items import Items
from .characters import CharacterData
from .zone import Zone


@mapper_registry.mapped
class BannedIPs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/banned_ips/
    """
    __tablename__ = "banned_ips"
    ip_address = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    """IP Address"""
    notes = Column(mysql.VARCHAR(32), nullable=True)
    """Ban reason"""


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
    """Unique Bug Identifier"""
    zone = Column(mysql.VARCHAR(32), nullable=False)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    name = Column(mysql.VARCHAR(64), nullable=False)
    """Player Name"""
    ui = Column(mysql.VARCHAR(128), nullable=False)
    """UI"""
    x = Column(mysql.FLOAT, nullable=False, default=0)
    """X Coordinate"""
    y = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Coordinate"""
    z = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Coordinate"""
    type = Column(mysql.VARCHAR(64), nullable=False)
    """Type"""
    flag = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False)
    """Flag"""
    target = Column(mysql.VARCHAR(64), nullable=True)
    """Target when reported"""
    bug = Column(mysql.VARCHAR(1024), nullable=False)
    """Bug reported"""
    date = Column(mysql.DATE, nullable=False)
    """Date when reported"""
    status = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Account Status of Reporter (see https://docs.eqemu.io/server/player/status-levels)"""


@mapper_registry.mapped
class ChatChannels:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/chatchannels/
    """
    __tablename__ = "chat_channels"
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    """Name"""
    owner = Column(mysql.VARCHAR(64), nullable=False)
    """Owner Character Identifier (see https://docs.eqemu.io/schema/characters/character_data/)"""
    password = Column(mysql.VARCHAR(64), nullable=False)
    """Password"""
    minstatus = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    """Minimum Status (see https://docs.eqemu.io/server/player/status-levels)"""


@mapper_registry.mapped
class CommandSettings:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/command_settings/
    """
    __tablename__ = "command_settings"
    command = Column(mysql.VARCHAR(128), nullable=False, primary_key=True)
    """Unique Command Identifier"""
    access = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Required Status (see https://docs.eqemu.io/server/player/status-levels)"""
    aliases = Column(mysql.VARCHAR(256), nullable=False)
    """Aliases"""


@mapper_registry.mapped
class DBVersion:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/db_version/
    """
    __tablename__ = "db_version"
    version = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=True, default=0)
    """Primary Key is not actually defined in SQL"""
#    bots_version = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    """Bots Version (only exists if bots are enabled on your server)"""


@mapper_registry.mapped
class DiscoveredItems:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/discovered_items/
    """
    __tablename__ = "discovered_items"
    item_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Items.id),
                     primary_key=True, nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    char_name = Column(mysql.VARCHAR(64), ForeignKey(CharacterData.name), nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    discovered_date = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Discovered Date UNIX Timestamp"""
    account_status = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Account Status (see https://docs.eqemu.io/server/player/status-levels)"""


'''
@mapper_registry.mapped
class DiscordWebhooks:
    """
    New - does not seem to exist in default db
    
    https://docs.eqemu.io/schema/admin/discord_webhooks/
    """
    __tablename__ = "discord_webhooks"
    id = Column(mysql.INTEGER(display_width=11))
    webhook_name = Column(mysql.VARCHAR)
    webhook_url = Column(mysql.VARCHAR)
    created_at = Column(mysql.DATETIME)
    deleted_at = Column(mysql.DATETIME)
'''


@mapper_registry.mapped
class EQTime:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/eqtime/
    """
    __tablename__ = "eqtime"
    minute = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Minute; Primary Key is not actually defined in SQL"""
    hour = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Hour; Primary Key is not actually defined in SQL"""
    day = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Day; Primary Key is not actually defined in SQL"""
    month = Column(mysql.TINYINT(display_width=4), primary_key=True, nullable=False, default=0)
    """Month; Primary Key is not actually defined in SQL"""
    year = Column(mysql.INTEGER(display_width=4), primary_key=True, nullable=False, default=0)
    """Year; Primary Key is not actually defined in SQL"""
    realtime = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=False, default=0)
    """Real Time; Primary Key is not actually defined in SQL"""


@mapper_registry.mapped
class EventLog:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/eventlog/
    """
    __tablename__ = "eventlog"
    id = Column(mysql.INTEGER(10, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Event Identifier"""
    accountname = Column(mysql.VARCHAR(30), ForeignKey(Account.name), nullable=False)
    """Account Name (see https://docs.eqemu.io/schema/account/account/)"""
    accountid = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(Account.id), nullable=True, default=0)
    """Account Identifier (see https://docs.eqemu.io/schema/account/account/)"""
    status = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    """Status (see https://docs.eqemu.io/server/player/status-levels)"""
    charname = Column(mysql.VARCHAR(64), ForeignKey(CharacterData.name), nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    target = Column(mysql.VARCHAR(64), nullable=True, default="None")
    """Target"""
    time = Column(mysql.TIMESTAMP, nullable=False, default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    """Time Timestamp"""
    descriptiontype = Column(mysql.TEXT, nullable=False)
    """Description Type"""
    description = Column(mysql.TEXT, nullable=False, default=None)
    """Description"""
    event_nid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Description"""


@mapper_registry.mapped
class GMIPs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/gm_ips/
    """
    __tablename__ = "gm_ips"
    name = Column(mysql.VARCHAR(64), nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    account_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True)
    """Account Identifier (see https://docs.eqemu.io/schema/account/account/)"""
    ip_address = Column(mysql.VARCHAR(15), nullable=False, primary_key=True)
    """IP Address (see https://docs.eqemu.io/schema/account/account_ip/)"""


@mapper_registry.mapped
class Hackers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/hackers/
    """
    __tablename__ = "hackers"
    id = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Hacker Identifier"""
    account = Column(mysql.TEXT, nullable=False)
    """Account Identifier (see https://docs.eqemu.io/schema/account/account/)"""
    name = Column(mysql.TEXT, nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    hacked = Column(mysql.TEXT, nullable=False)
    """Hacked"""
    zone = Column(mysql.TEXT, nullable=True)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    date = Column(mysql.TIMESTAMP, nullable=False, default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    """Date Timestamp"""


@mapper_registry.mapped
class IPExemptions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/ip_exemptions/
    """
    __tablename__ = "ip_exemptions"
    exemption_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    """Exemption Identifier"""
    exemption_ip = Column(mysql.VARCHAR(255), nullable=True)
    """Exemption IP Address (see https://docs.eqemu.io/schema/account/account_ip/)"""
    exemption_amount = Column(mysql.INTEGER(display_width=11), nullable=True)
    """Exemption Amount"""


@mapper_registry.mapped
class LevelExpMods:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/level_exp_mods/
    """
    __tablename__ = "level_exp_mods"
    level = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    """Level"""
    exp_mod = Column(mysql.FLOAT, nullable=True)     # Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%
    """Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%"""
    aa_exp_mod = Column(mysql.FLOAT, nullable=True)  # AA Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%
    """AA Experience Modifier: 0.5 = 50%, 1 = 100%, 1.5 = 150%"""


@mapper_registry.mapped
class LogSysCategories:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/logsys_categories/
    """
    __tablename__ = "logsys_categories"
    log_category_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Log Category Identifier"""
    log_category_description = Column(mysql.VARCHAR(150), nullable=True)
    """Log Category Description"""
    log_to_console = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Log to Console: 0 = False, 1 = True"""
    log_to_file = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Log to File: 0 = False, 1 = True"""
    log_to_gmsay = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Log to GMSay: 0 = False, 1 = True"""


@mapper_registry.mapped
class NameFilter:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/name_filter/
    """
    __tablename__ = "name_filter"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Name Filter Identifier"""
    name = Column(mysql.VARCHAR(30), nullable=False, index=True)  # index=True should set Key column to "MUL"
    """Name"""


@mapper_registry.mapped
class PerlEventExportSettings:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/perl_event_export_settings/
    """
    __tablename__ = "perl_event_export_settings"
    event_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True)
    """Unique Perl Event Identifier"""
    event_description = Column(mysql.VARCHAR(150), nullable=True)
    """Event Description"""
    export_qglobals = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Export QGlobals: 0 = False, 1 = True"""
    export_mob = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Export Mob: 0 = False, 1 = True"""
    export_zone = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Export Zone: 0 = False, 1 = True"""
    export_item = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Export Item: 0 = False, 1 = True"""
    export_event = Column(mysql.SMALLINT(display_width=11), nullable=True, default=0)
    """Export Event: 0 = False, 1 = True"""


@mapper_registry.mapped
class Petitions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/petitions/
    """
    __tablename__ = "petitions"
    dib = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, autoincrement="auto")
    """Unknown"""
    petid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, index=True, default=0)
    """Unique Petition Entry Identifier"""
    charname = Column(mysql.VARCHAR(32), nullable=False)
    """Character Name (see https://docs.eqemu.io/schema/characters/character_data/)"""
    accountname = Column(mysql.VARCHAR(32), nullable=False)
    """Account Name (see https://docs.eqemu.io/schema/account/account/)"""
    lastgm = Column(mysql.VARCHAR(32), nullable=False)
    """Last GM"""
    petitiontext = Column(mysql.TEXT, nullable=False)
    """Petition Text"""
    gmtext = Column(mysql.TEXT, nullable=True)
    """GM Text"""
    zone = Column(mysql.VARCHAR(32), nullable=False)
    """Zone Short Name (see https://docs.eqemu.io/server/zones/zone-list)"""
    urgency = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Urgency"""
    charclass = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Character Class (see https://docs.eqemu.io/server/player/class-list)"""
    charrace = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Character Race (see https://docs.eqemu.io/server/npc/race-list)"""
    charlevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Character Level"""
    checkouts = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Checkouts"""
    unavailables = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Unavailables"""
    ischeckedout = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Is Checked Out: 0 = False, 1 = True"""
    senttime = Column(mysql.BIGINT(display_width=11), nullable=False, default=0)
    """Sent Time UNIX Timestamp"""


@mapper_registry.mapped
class ProfanityList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/profanity_list/
    """
    __tablename__ = "profanity_list"
    word = Column(mysql.VARCHAR(16), primary_key=True, nullable=False)
    """Word; Primary Key is not actually defined in SQL"""


@mapper_registry.mapped
class Reports:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/reports/
    """
    __tablename__ = "reports"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Report Identifier"""
    name = Column(mysql.VARCHAR(64), nullable=True)
    """Name"""
    reported = Column(mysql.VARCHAR(64), nullable=True)
    """Reported"""
    reported_text = Column(mysql.TEXT, nullable=True)
    """Reported Text"""


@mapper_registry.mapped
class SayLink:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/saylink/
    """
    __tablename__ = "saylink"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, autoincrement="auto")
    """Unique Saylink Identifier"""
    phrase = Column(mysql.VARCHAR(64), nullable=False, index=True)
    """Phrase"""


@mapper_registry.mapped
class StartZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/start_zones/
    """
    __tablename__ = "start_zones"
    x = Column(mysql.FLOAT, nullable=False, default=0)
    """X Coordinate"""
    y = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Coordinate"""
    z = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Coordinate"""
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    """Heading Coordinate"""
    zone_id = Column(mysql.INTEGER(display_width=4), ForeignKey(Zone.zoneidnumber), nullable=False, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    bind_id = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Bind Identifier"""
    player_choice = Column(mysql.INTEGER(display_width=2), nullable=False, primary_key=True, default=0)
    """Player Choice"""
    player_class = Column(mysql.INTEGER(display_width=2), nullable=False, primary_key=True, default=0)
    """Player Class (see https://docs.eqemu.io/server/player/class-list)"""
    player_deity = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    """Player Deity (see https://docs.eqemu.io/server/player/deity-list)"""
    player_race = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    """Player Race (see https://docs.eqemu.io/server/npc/race-list)"""
    start_zone = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    bind_x = Column(mysql.FLOAT, nullable=False, default=0)
    """Bind X Coordinate"""
    bind_y = Column(mysql.FLOAT, nullable=False, default=0)
    """Bind Y Coordinate"""
    bind_z = Column(mysql.FLOAT, nullable=False, default=0)
    """Bind Z Coordinate"""
    select_rank = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=50)
    """Select Rank: Always 50"""
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)

    zone = relationship("Zone", foreign_keys=[zone_id], uselist=False)
    """Relationship Type: One-to-One, Local Key: zone_id, Relates to Table: zone, Foreign Key: zoneidnumber"""


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
    """Unique Starting Items Entry Identifier"""
    race = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    """Race (see https://docs.eqemu.io/server/npc/race-list): 0 = All"""
    _class = Column("class", mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Class (see https://docs.eqemu.io/server/player/class-list): 0 = All"""
    deityid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Deity (see https://docs.eqemu.io/server/player/deity-list): 0 = All"""
    zoneid = Column(mysql.INTEGER(display_width=11), ForeignKey(Zone.zoneidnumber), nullable=False, default=0)
    """Zone Identifier (see https://docs.eqemu.io/server/zones/zone-list)"""
    itemid = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id), nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    item_charges = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """Item Charges"""
    gm = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    """GM: 0 = False, 1 = True"""
    slot = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=-1)
    """Slot (see https://docs.eqemu.io/server/inventory/inventory-slots)"""
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)

    zone = relationship("Zone", uselist=False)
    """Relationship Type: One-to-One, Local Key: zone_id, Relates to Table: zone, Foreign Key: zoneidnumber"""
    items = relationship("Items", uselist=False)
    """Relationship Type: One-to-One, Local Key: itemid, Relates to Table: items, Foreign Key: id"""


@mapper_registry.mapped
class Variables:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/variables/
    """
    __tablename__ = "variables"
    varname = Column(mysql.VARCHAR(35), nullable=False, primary_key=True)
    """Variable Name"""
    value = Column(mysql.TEXT, nullable=False)
    """Value"""
    information = Column(mysql.TEXT, nullable=False)
    """Information"""
    ts = Column(mysql.TIMESTAMP, nullable=False, default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    """Timestamp"""


@mapper_registry.mapped
class VeteranRewardTemplates:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/admin/veteran_reward_templates/
    """
    __tablename__ = "veteran_reward_templates"
    claim_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    """Unique Claim Identifier"""
    name = Column(mysql.VARCHAR(64), nullable=False)
    """Name"""
    item_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    charges = Column(mysql.SMALLINT(display_width=5, unsigned=True))
    """Charges"""
    reward_slot = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True)
    """Reward Slot"""
