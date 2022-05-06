from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class CharCreateCombinations:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/char_create_combinations/
    """
    __tablename__ = "char_create_combinations"
    allocation_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    race = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    _class = Column("class", mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True,
                    default=None)
    deity = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    start_zone = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    expansions_req = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class CharCreatePointAllocations:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/char_create_point_allocations/
    """
    __tablename__ = "char_create_point_allocations"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    base_str = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_sta = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_dex = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_agi = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_int = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_wis = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    base_cha = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_str = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_sta = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_dex = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_agi = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_int = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_wis = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    alloc_cha = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)


@mapper_registry.mapped
class CharRecipeList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/char_recipe_list/
    """
    __tablename__ = "char_recipe_list"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    recipe_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    madecount = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class CharacterActivities:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_activities/
    """
    __tablename__ = "character_activities"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    activityid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    donecount = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    completed = Column(mysql.TINYINT(display_width=1), nullable=True, default=0)


@mapper_registry.mapped
class CharacterAltCurrency:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_alt_currency/
    """
    __tablename__ = "character_alt_currency"
    char_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    currency_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    amount = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)


@mapper_registry.mapped
class CharacterAlternateAbilities:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_alternate_abilities/
    """
    __tablename__ = "character_alternate_abilities"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    aa_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    aa_value = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)
    charges = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class CharacterAuras:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_auras/
    """
    __tablename__ = "character_auras"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None)
    slot = Column(mysql.TINYINT(display_width=10), nullable=False, primary_key=True, default=None)
    spell_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=None)


@mapper_registry.mapped
class CharacterBandolier:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_bandolier/
    """
    __tablename__ = "character_bandolier"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    bandolier_id = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    bandolier_slot = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    item_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    icon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    bandolier_name = Column(mysql.VARCHAR(32), nullable=False, default=0)


@mapper_registry.mapped
class CharacterBind:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_bind/
    """
    __tablename__ = "character_bind"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True,
                default=None, auto_increment="auto")
    slot = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    zone_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)
    instance_id = Column(mysql.MEDIUMINT(display_width=11, unsigned=True), nullable=False, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)


@mapper_registry.mapped
class CharacterBuffs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_buffs/
    """
    __tablename__ = "character_buffs"
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                          primary_key=True, default=None)
    slot_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False,
                     primary_key=True, default=None)
    spell_id = Column(mysql.SMALLINT(display_width=10, unsigned=True), nullable=False, default=0)
    caster_level = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=None)
    caster_name = Column(mysql.VARCHAR(64), nullable=False, default=None)
    ticsremaining = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    counters = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    numhits = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    melee_rune = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    magic_rune = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)
    persistent = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=None)
    dot_rune = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    caston_x = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    caston_y = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    caston_z = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    ExtraDIChance = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    instrument_mod = Column(mysql.INTEGER(display_width=10), nullable=False, default=10)


@mapper_registry.mapped
class CharacterCorpseItems:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_corpse_items/
    """
    __tablename__ = "character_corpse_items"


@mapper_registry.mapped
class CharacterCorpses:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_corpses/
    """
    __tablename__ = "character_corpses"


@mapper_registry.mapped
class CharacterCurrency:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_currency/
    """
    __tablename__ = "character_currency"


@mapper_registry.mapped
class CharacterData:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_data/
    """
    __tablename__ = "character_data"


@mapper_registry.mapped
class CharacterDisciplines:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_disciplines/
    """
    __tablename__ = "character_disciplines"


@mapper_registry.mapped
class CharacterEnabledTasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_enabledtasks/
    """
    __tablename__ = "character_enabledtasks"


@mapper_registry.mapped
class CharacterExpModifiers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_exp_modifiers/
    """
    __tablename__ = "character_exp_modifiers"


@mapper_registry.mapped
class CharacterExpeditionLockouts:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_expedition_lockouts/
    """
    __tablename__ = "character_expedition_lockouts"


@mapper_registry.mapped
class CharacterInspectMessages:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_inspect_messages/
    """
    __tablename__ = "character_inspect_messages"


@mapper_registry.mapped
class CharacterInstanceSafereturns:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_instance_safereturns/
    """
    __tablename__ = "character_instance_safereturns"


@mapper_registry.mapped
class CharacterItemRecast:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_item_recast/
    """
    __tablename__ = "character_item_recast"


@mapper_registry.mapped
class CharacterLanguages:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_languages/
    """
    __tablename__ = "character_languages"


@mapper_registry.mapped
class CharacterLeadershipAbilities:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_leadership_abilities/
    """
    __tablename__ = "character_leadership_abilities"


@mapper_registry.mapped
class CharacterMaterial:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_material/
    """
    __tablename__ = "character_material"


@mapper_registry.mapped
class CharacterMemmedSpells:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_memmed_spells/
    """
    __tablename__ = "character_memmed_spells"


@mapper_registry.mapped
class CharacterPetBuffs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_buffs/
    """
    __tablename__ = "character_pet_buffs"


@mapper_registry.mapped
class CharacterPetInfo:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_info/
    """
    __tablename__ = "character_pet_info"


@mapper_registry.mapped
class CharacterPetInventory:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_inventory/
    """
    __tablename__ = "character_pet_inventory"


@mapper_registry.mapped
class CharacterPotionBelt:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_potionbelt/
    """
    __tablename__ = "character_potionbelt"


@mapper_registry.mapped
class CharacterSkills:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_skills/
    """
    __tablename__ = "character_skills"


@mapper_registry.mapped
class CharacterSpells:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_spells/
    """
    __tablename__ = "character_spells"


@mapper_registry.mapped
class CharacterTasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_tasks/
    """
    __tablename__ = "character_tasks"


@mapper_registry.mapped
class CharacterTaskTimers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_task_timers/
    """
    __tablename__ = "character_task_timers"


@mapper_registry.mapped
class CharacterTribute:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_tribute/
    """
    __tablename__ = "character_tribute"


@mapper_registry.mapped
class Friends:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/friends/
    """
    __tablename__ = "friends"
    charid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    type = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, primary_key=True, default=1)
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True, default=None)


@mapper_registry.mapped
class Keyring:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/keyring/
    """
    __tablename__ = "keyring"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class LFGuild:
    """
    EQEMU Docs UR: https://docs.eqemu.io/schema/characters/lfguild/
    """
    __tablename__ = "lfguild"
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    name = Column(mysql.VARCHAR(32), nullable=False, primary_key=True, default=None)
    comment = Column(mysql.VARCHAR(256), nullable=False, default=None)
    fromlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    tolevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    classes = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    aacount = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    timezone = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    timeposted = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class Mail:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/mail/
    """
    __tablename__ = "mail"
    msgid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True,
                   default=None, auto_increment="auto")
    charid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, unique=False,
                    primary_key=True, default=0)
    timestamp = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    _from = Column("from", mysql.VARCHAR(100), nullable=False)
    subject = Column(mysql.VARCHAR(200), nullable=False)
    body = Column(mysql.TEXT, nullable=False, default=None)
    to = Column(mysql.TEXT, nullable=False, default=None)
    status = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)


@mapper_registry.mapped
class PlayerTitlesets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/player_titlesets/
    """
    __tablename__ = "player_titlesets"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True,
                default=None, auto_increment="auto")
    char_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=None)
    title_set = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=None)
