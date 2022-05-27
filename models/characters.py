from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql

from meta import Base
from .items import Items


class CharCreateCombinations(Base):
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


class CharCreatePointAllocations(Base):
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


class CharRecipeList(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/char_recipe_list/
    """
    __tablename__ = "char_recipe_list"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    recipe_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    madecount = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


class CharacterActivities(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_activities/
    """
    __tablename__ = "character_activities"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    activityid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    donecount = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    completed = Column(mysql.TINYINT(display_width=1), nullable=True, default=0)


class CharacterAltCurrency(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_alt_currency/
    """
    __tablename__ = "character_alt_currency"
    char_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    currency_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    amount = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=None)


class CharacterAlternateAbilities(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_alternate_abilities/
    """
    __tablename__ = "character_alternate_abilities"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    aa_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    aa_value = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)
    charges = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterAuras(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_auras/
    """
    __tablename__ = "character_auras"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None)
    slot = Column(mysql.TINYINT(display_width=10), nullable=False, primary_key=True, default=None)
    spell_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=None)


class CharacterBandolier(Base):
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


class CharacterBind(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_bind/
    """
    __tablename__ = "character_bind"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True,
                default=None, autoincrement="auto")
    slot = Column(mysql.INTEGER(display_width=4), nullable=False, primary_key=True, default=0)
    zone_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)
    instance_id = Column(mysql.MEDIUMINT(display_width=11, unsigned=True), nullable=False, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)


class CharacterBuffs(Base):
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


class CharacterCorpses(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_corpses/
    """
    __tablename__ = "character_corpses"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True,
                default=None, autoincrement="auto")
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    charname = Column(mysql.VARCHAR(64), nullable=False)
    zone_id = Column(mysql.SMALLINT(display_width=5), nullable=False, unique=False, primary_key=True, default=0)
    instance_id = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False,
                         unique=False, primary_key=True, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    time_of_death = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    guild_consent_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    is_rezzed = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=True, default=0)
    is_buried = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    was_at_graveyard = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    is_locked = Column(mysql.TINYINT(display_width=11), nullable=True, default=0)
    exp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    size = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    level = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    race = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    gender = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    _class = Column("class", mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    deity = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    texture = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    helm_texture = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    copper = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    silver = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    gold = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    platinum = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    hair_color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    beard_color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    eye_color_1 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    eye_color_2 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    hair_style = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    face = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    beard = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    drakkin_heritage = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    drakkin_tattoo = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    drakkin_details = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_1 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_2 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_3 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_4 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_5 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_6 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_7 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_8 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    wc_9 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)


class CharacterCorpseItems(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_corpse_items/
    """
    __tablename__ = "character_corpse_items"
    corpse_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(CharacterCorpses.id),
                       primary_key=True, nullable=False, default=None)
    """Corpse Identifier (see https://docs.eqemu.io/schema/characters/character_corpses/)"""
    equip_slot = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=None)
    """Equipment Slot"""
    item_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(Items.id),
                     nullable=True, default=None)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
    charges = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=None)
    """Item Charges"""
    aug_1 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 1"""
    aug_2 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 2"""
    aug_3 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 3"""
    aug_4 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 4"""
    aug_5 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 5"""
    aug_6 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    """Item Augment Slot 6"""
    attuned = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Item Attuned: 0 = False, 1 = True"""


class CharacterCurrency(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_currency/
    """
    __tablename__ = "character_currency"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    platinum = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    gold = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    silver = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    copper = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    platinum_bank = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    gold_bank = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    silver_bank = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    copper_bank = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    platinum_cursor = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    gold_cursor = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    silver_cursor = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    copper_cursor = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    radiant_crystals = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    career_radiant_crystals = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ebon_crystals = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    career_ebon_crystals = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterData(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_data/
    """
    __tablename__ = "character_data"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    account_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, unique=False,
                        primary_key=True, default=0)
    name = Column(mysql.VARCHAR(64), nullable=False, unique=True)
    last_name = Column(mysql.VARCHAR(64), nullable=False)
    title = Column(mysql.VARCHAR(32), nullable=False)
    suffix = Column(mysql.VARCHAR(32), nullable=False)
    zone_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    zone_instance = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    y = Column(mysql.FLOAT, nullable=False, default=0)
    x = Column(mysql.FLOAT, nullable=False, default=0)
    z = Column(mysql.FLOAT, nullable=False, default=0)
    heading = Column(mysql.FLOAT, nullable=False, default=0)
    gender = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    race = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)
    _class = Column("class", mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    level = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    deity = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    birthday = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    last_login = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    time_played = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    level2 = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    anon = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    gm = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    face = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    hair_color = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    hair_style = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    beard = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    beard_color = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    eye_color_1 = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    eye_color_2 = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    drakkin_heritage = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    drakkin_tatoo = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    drakkin_details = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ability_time_seconds = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    ability_number = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    ability_time_minutes = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    ability_time_hours = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    exp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    aa_points_spent = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    aa_exp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    aa_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    group_leadership_exp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    raid_leadership_exp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    group_leadership_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    raid_leadership_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    cur_hp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    mana = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    endurance = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    intoxication = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    str = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    sta = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    cha = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    dex = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    int = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    agi = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    wis = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    zone_change_count = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    toxicity = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    hunger_level = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    thirst_level = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ability_up = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_guk = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_mir = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_mmc = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_ruj = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_tak = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    ldon_points_available = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    tribute_time_remaining = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    career_tribute_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    tribute_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    tribute_active = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_status = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_kills = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_deaths = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_current_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_career_points = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_best_kill_streak = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_worst_death_streak = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_current_kill_streak = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp2 = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pvp_type = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    show_helm = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    group_auto_consent = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    raid_auto_consent = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    guild_auto_consent = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    leadership_exp_on = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    RestTimer = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    air_remaining = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    autosplit_enabled = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    lfp = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    lfg = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    mailkey = Column(mysql.CHAR(16), nullable=False)
    xtargets = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=5)
    firstlogon = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    e_aa_effects = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    e_percent_to_aa = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    e_expended_aa_spent = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    aa_points_spent_old = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    aa_points_old = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    e_last_invsnapshot = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    deleted_at = Column(mysql.DATETIME, nullable=True, default=None)


class CharacterDisciplines(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_disciplines/
    """
    __tablename__ = "character_disciplines"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slot_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    disc_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterEnabledTasks(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_enabledtasks/
    """
    __tablename__ = "character_enabledtasks"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)


class CharacterExpModifiers(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_exp_modifiers/
    """
    __tablename__ = "character_exp_modifiers"
    character_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    zone_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    aa_modifier = Column(mysql.FLOAT, nullable=False, default=None)
    exp_modifier = Column(mysql.FLOAT, nullable=False, default=None)


"""
class CharacterExpeditionLockouts(Base):
    '''
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_expedition_lockouts/
    '''
    
    __tablename__ = "character_expedition_lockouts"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                          unique=False, primary_key=True, default=None)
    expedition_name = Column(mysql.VARCHAR(128), nullable=False, default=None)
    event_name = Column(mysql.VARCHAR(256), nullable=False, default=None)
    expire_time = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP")
    duration = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    from_expedition_uuid = Column(mysql.VARCHAR(36), nullable=False, default=None)
"""""


class CharacterInspectMessages(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_inspect_messages/
    """
    __tablename__ = "character_inspect_messages"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    inspect_message = Column(mysql.VARCHAR(255), nullable=False)


class CharacterInstanceSafereturns(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_instance_safereturns/
    """
    __tablename__ = "character_instance_safereturns"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, unique=True, default=None)
    instance_zone_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    instance_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    safe_zone_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    safe_x = Column(mysql.FLOAT, nullable=False, default=0)
    safe_y = Column(mysql.FLOAT, nullable=False, default=0)
    safe_z = Column(mysql.FLOAT, nullable=False, default=0)
    safe_heading = Column(mysql.FLOAT, nullable=False, default=0)


class CharacterItemRecast(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_item_recast/
    """
    __tablename__ = "character_item_recast"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    recast_type = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    timestamp = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterLanguages(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_languages/
    """
    __tablename__ = "character_languages"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    lang_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    value = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterLeadershipAbilities(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_leadership_abilities/
    """
    __tablename__ = "character_leadership_abilities"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slot = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    rank = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterMaterial(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_material/
    """
    __tablename__ = "character_material"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    slot = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    blue = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    green = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    red = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    use_tint = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    color = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterMemmedSpells(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_memmed_spells/
    """
    __tablename__ = "character_memmed_spells"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slot_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    spell_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterPetBuffs(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_buffs/
    """
    __tablename__ = "character_pet_buffs"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    pet = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    slot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    spell_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    caster_level = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    castername = Column(mysql.VARCHAR(64), nullable=False)
    ticsremaining = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    counters = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    numhits = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    rune = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    instrument_mod = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=10)


class CharacterPetInfo(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_info/
    """
    __tablename__ = "character_pet_info"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    pet = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    petname = Column(mysql.VARCHAR(64), nullable=False)
    petpower = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    spell_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    hp = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    size = Column(mysql.FLOAT, nullable=False, default=0)
    taunting = Column(mysql.TINYINT(display_width=1), nullable=False, default=1)


class CharacterPetInventory(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_pet_inventory/
    """
    __tablename__ = "character_pet_inventory"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    pet = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    slot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)


class CharacterPotionBelt(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_potionbelt/
    """
    __tablename__ = "character_potionbelt"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    potion_id = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    item_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    icon = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterSkills(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_skills/
    """
    __tablename__ = "character_skills"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    skill_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    value = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterSpells(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_spells/
    """
    __tablename__ = "character_spells"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    slot_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    spell_id = Column(mysql.SMALLINT(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterTasks(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_tasks/
    """
    __tablename__ = "character_tasks"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    slot = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class CharacterTaskTimers(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_task_timers/
    """
    __tablename__ = "character_task_timers"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    character_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                          unique=False, primary_key=True, default=0)
    task_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                     unique=False, primary_key=True, default=0)
    timer_type = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    expire_time = Column(mysql.DATETIME, nullable=False, default="CURRENT_TIMESTAMP")


class CharacterTribute(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/character_tribute/
    """
    __tablename__ = "character_tribute"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, unique=False,
                primary_key=True, default=0)
    tier = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)
    tribute = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


class Friends(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/friends/
    """
    __tablename__ = "friends"
    charid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=None)
    type = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, primary_key=True, default=1)
    name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True, default=None)


class KeyRing(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/keyring/
    """
    __tablename__ = "keyring"
    char_id = Column(mysql.INTEGER(display_width=11), ForeignKey(CharacterData.id),
                     primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in sql"""
    item_id = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                     primary_key=True, nullable=False, default=0)
    """Primary Key is not actually defined in sql"""


class LFGuild(Base):
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


class Mail(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/mail/
    """
    __tablename__ = "mail"
    msgid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True,
                   default=None, autoincrement="auto")
    charid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, unique=False,
                    primary_key=True, default=0)
    timestamp = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    _from = Column("from", mysql.VARCHAR(100), nullable=False)
    subject = Column(mysql.VARCHAR(200), nullable=False)
    body = Column(mysql.TEXT, nullable=False, default=None)
    to = Column(mysql.TEXT, nullable=False, default=None)
    status = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)


class PlayerTitlesets(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/characters/player_titlesets/
    """
    __tablename__ = "player_titlesets"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True,
                default=None, autoincrement="auto")
    char_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=None)
    title_set = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=None)
