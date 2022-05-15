from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .factions import FactionList
from .alternate_currency import AlternateCurrency
from .merchants import MerchantList
from .spawns import SpawnEntry


@mapper_registry.mapped
class NPCEmotes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_emotes/
    """
    __tablename__ = "npc_emotes"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None, autoincrement="auto")
    emoteid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                     unique=False, primary_key=True, default=0)
    event_ = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    text = Column(mysql.VARCHAR(512), nullable=False, default=None)


@mapper_registry.mapped
class NPCFaction:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_faction/
    """
    __tablename__ = "npc_faction"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    primaryfaction = Column(mysql.INTEGER(display_width=11), ForeignKey(FactionList.id), nullable=False, default=0)
    ignore_primary_assist = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)

    npc_faction_entries = relationship("NPCFactionEntries", back_populates="npc_faction")
    """Relationship Type: Has-Many, Local Key: id, Relates to Table: npc_faction_entries, Foreign Key: npc_faction_id"""


@mapper_registry.mapped
class NPCFactionEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_faction_entries/
    """
    __tablename__ = "npc_faction_entries"
    npc_faction_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(NPCFaction.id), primary_key=True,
                            nullable=False, default=0)
    """NPC Faction Identifier"""
    faction_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(FactionList.id), primary_key=True,
                        nullable=False, default=0)
    """Faction Identifier"""
    value = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Value"""
    npc_value = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    """NPC Value: -1 = Attack, 0 = Neutral, 1 = Assist"""
    temp = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    """
    Temporary: 0 = Faction is permanent, player receives a message, 1 = Faction is temporary, player does not 
    receive a message, 2 = Faction is temporary, player receives a message, 3 = Faction is permanent, but player does 
    not receive a message.
    """

    npc_faction = relationship("NPCFaction", back_populates="npc_faction_entries")


@mapper_registry.mapped
class NPCScaleGlobalBase:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_scale_global_base/
    """
    __tablename__ = "npc_scale_global_base"
    type = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    level = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    ac = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    hp = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    accuracy = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    slow_mitigation = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    attack = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    strength = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    stamina = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    dexterity = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    agility = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    intelligence = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    wisdom = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    charisma = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    magic_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    cold_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    fire_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    poison_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    disease_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    corruption_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    physical_resist = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    min_dmg = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    max_dmg = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    hp_regen_rate = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    attack_delay = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    spell_scale = Column(mysql.INTEGER(display_width=11), nullable=True, default=100)
    heal_scale = Column(mysql.INTEGER(display_width=11), nullable=True, default=100)
    special_abilities = Column(mysql.TEXT, nullable=True, default=None)


@mapper_registry.mapped
class NPCSpells:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells/
    """
    __tablename__ = "npc_spells"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique NPC Spell Set Identifier"""
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    """NPC Spell Set Name"""
    parent_list = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """
    Inherit all the spells from this list, and merge them with our spells.  Only one level of inheritance is allowed,
    so your parent's parent will not be included.
    """
    attack_proc = Column(mysql.SMALLINT(5), nullable=False, default=-1)
    """
    The combat proc that an NPC with this spell set will add to their list of procs.
    Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)
    """
    proc_chance = Column(mysql.TINYINT(display_width=3), nullable=False, default=3)
    """Proc Chance: 0 = Never, 100 = Always"""
    range_proc = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    """The ranged proc that an NPC with this spell set will add to their list of procs."""
    rproc_chance = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Ranged Proc Chance: 0 = Never, 100 = Always"""
    defensive_proc = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    """The defensive proc that an NPC with this spell set will add to their list of procs."""
    dproc_chance = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Defensive Proc Chance: 0 = Never, 100 = Always"""
    fail_recast = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Fail Recast"""
    engaged_no_sp_recast_min = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    engaged_no_sp_recast_max = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    engaged_b_self_chance = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    engaged_b_other_chance = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    engaged_d_chance = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    pursue_no_sp_recast_min = Column(mysql.INTEGER(display_width=3, unsigned=True), nullable=False, default=0)
    pursue_no_sp_recast_max = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    pursue_d_chance = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    idle_no_sp_recast_min = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    idle_no_sp_recast_max = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    idle_b_chance = Column(mysql.TINYINT(display_width=11, unsigned=True), nullable=False, default=0)

    npc_spells_entries = relationship("NPCSpellsEntries", back_populates="npc_spells")


@mapper_registry.mapped
class NPCSpellsEffects:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_effects/
    """
    __tablename__ = "npc_spells_effects"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    parent_list = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)

    npc_spells_effects_entries = relationship("NPCSpellsEffectsEntries", back_populates="npc_spells_effects")


@mapper_registry.mapped
class NPCSpellsEffectsEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_effects_entries/
    """
    __tablename__ = "npc_spells_effects_entries"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique Spell Effect Entry Identifier"""
    npc_spells_effects_id = Column(mysql.INTEGER(display_width=11), ForeignKey(NPCSpellsEffects.id), nullable=False,
                                   unique=False, primary_key=True, default=0)
    """NPC Spells Effects Identifier (see https://docs.eqemu.io/schema/npcs/npc_spells_effects/)"""
    spell_effect_id = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Spell Effect Identifier (see https://docs.eqemu.io/server/spells/spell-effect-ids)"""
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Minimum Level"""
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=255)
    """Maximum Level"""
    se_base = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Spell Effect Base"""
    se_limit = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Spell Effect Limit"""
    se_max = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Spell Effect Maximum"""

    npc_spells_effects = relationship("NPCSpellsEffects", back_populates="npc_spells_effects_entries")


@mapper_registry.mapped
class NPCSpellsEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_entries/
    """
    __tablename__ = "npc_spells_entries"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    """Unique NPC Spell Entry Identifier"""
    npc_spells_id = Column(mysql.INTEGER(display_width=11), ForeignKey(NPCSpells.id), nullable=False,
                           unique=False, primary_key=True, default=0)
    """Unique NPC Spell Set Identifier"""
    spellid = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    """Spell Identifier"""
    type = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Spell Type Bitmask"""
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Minimum Level"""
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=255)
    """Maximum Level"""
    manacost = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    """Mana Cost"""
    recast_delay = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    """Recast Delay"""
    priority = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    """Priority: 0 = Innate, 1 = Highest Priority, 5 = Lower Priority, 10 = Even Lower Priority"""
    resist_adjust = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    """Resist Adjustment"""
    min_hp = Column(mysql.SMALLINT(display_width=5), nullable=True, default=0)
    """Minimum Health Percentage"""
    max_hp = Column(mysql.SMALLINT(display_width=5), nullable=True, default=0)
    """Maximum Health Percentage"""

    npc_spells = relationship("NPCSpells", back_populates="npc_spells_entries")


@mapper_registry.mapped
class NPCTypesTint:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_types_tint/
    """
    __tablename__ = "npc_types_tint"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    tint_set_name = Column(mysql.TEXT, nullable=False, default=None)
    red1h = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn1h = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu1h = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red2c = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn2c = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu2c = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red3a = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn3a = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu3a = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red4b = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn4b = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu4b = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red5g = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn5g = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu5g = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red6l = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn6l = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu6l = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red7f = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn7f = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu7f = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red8x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn8x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu8x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    red9x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    grn9x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    blu9x = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class NPCTypes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_types/
    """
    __tablename__ = "npc_types"
    id = Column(mysql.INTEGER(display_width=11), ForeignKey(SpawnEntry.npcID), primary_key=True,
                nullable=False, default=None, autoincrement="auto")
    name = Column(mysql.TEXT, nullable=False, default=None)
    lastname = Column(mysql.VARCHAR(32), nullable=True, default=None)
    level = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    race = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    class_ = Column("class", mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    bodytype = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    hp = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    gender = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    texture = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    helmtexture = Column(mysql.TINYINT(display_width=2, unsigned=True), nullable=False, default=0)
    herosforgemodel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    size = Column(mysql.FLOAT, nullable=False, default=0)
    hp_regen_rate = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    hp_regen_per_second = Column(mysql.BIGINT(display_width=11), nullable=True, default=0)
    mana_regen_rate = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    loottable_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    merchant_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(MerchantList.merchantid),
                         nullable=False, default=0)
    alt_currency_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(AlternateCurrency.id),
                             nullable=False, default=0)
    npc_spells_id = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey(NPCSpells.id),
                           nullable=False, default=0)
    npc_spells_effects_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    npc_faction_id = Column(mysql.INTEGER(display_width=11), ForeignKey(NPCFaction.id),
                            nullable=False, default=0)
    adventure_template_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    trap_template = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    mindmg = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    maxdmg = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    attack_count = Column(mysql.SMALLINT(display_width=6), nullable=False, default=-1)
    npcspecialattks = Column(mysql.VARCHAR(36), nullable=False)
    special_abilities = Column(mysql.TEXT, nullable=True, default=None)
    aggroradius = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    assistradius = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    face = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_hairstyle = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_haircolor = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_eyecolor = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_eyecolor2 = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_beardcolor = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
    luclin_beard = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    drakkin_heritage = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    drakkin_tattoo = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    drakkin_details = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    armortint_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(NPCTypesTint.id),
                          nullable=False, default=0)
    armortint_red = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    armortint_green = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    armortint_blue = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    d_melee_texture1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    d_melee_texture2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ammo_idfile = Column(mysql.VARCHAR(30), nullable=False, default="IT10")
    prim_melee_type = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=28)
    sec_melee_type = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=28)
    ranged_type = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=7)
    runspeed = Column(mysql.FLOAT, nullable=False, default=0)
    MR = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    CR = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    DR = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    FR = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    PR = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    Corrup = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    PhR = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    see_invis = Column(mysql.SMALLINT(display_width=4, unsigned=True), nullable=False, default=0)
    see_invis_undead = Column(mysql.SMALLINT(display_width=4, unsigned=True), nullable=False, default=0)
    qglobal = Column(mysql.INTEGER(display_width=2, unsigned=True), nullable=False, default=0)
    AC = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    npc_aggro = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    spawn_limit = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    attack_speed = Column(mysql.FLOAT, nullable=False, default=0)
    attack_delay = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=30)
    findable = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    STR = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    STA = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    DEX = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    AGI = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    _INT = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=80)
    WIS = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    CHA = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=75)
    see_hide = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    see_improved_hide = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    trackable = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    isbot = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    exclude = Column(mysql.TINYINT(display_width=4), nullable=False, default=1)
    ATK = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=0)
    Accuracy = Column(mysql.MEDIUMINT(display_width=9), nullable=False, default=0)
    Avoidance = Column(mysql.MEDIUMINT(display_width=9, unsigned=True), nullable=False, default=0)
    slow_mitigation = Column(mysql.SMALLINT(display_width=4), nullable=False, default=0)
    version = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    maxlevel = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    scalerate = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    private_corpse = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    unique_spawn_by_name = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    underwater = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    isquest = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    emoteid = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(NPCEmotes.emoteid),
                     nullable=False, default=0)
    spellscale = Column(mysql.FLOAT, nullable=False, default=100)
    healscale = Column(mysql.FLOAT, nullable=False, default=100)
    no_target_hotkey = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    raid_target = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    armtexture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    bracertexture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    handtexture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    legtexture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    feettexture = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    light = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    walkspeed = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    peqid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    unique_ = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    fixed = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    ignore_despawn = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    show_name = Column(mysql.TINYINT(display_width=2), nullable=False, default=1)
    untargetable = Column(mysql.TINYINT(display_width=2), nullable=False, default=0)
    charm_ac = Column(mysql.SMALLINT(display_width=5), nullable=True, default=0)
    charm_min_dmg = Column(mysql.INTEGER(display_width=10), nullable=True, default=0)
    charm_max_dmg = Column(mysql.INTEGER(display_width=10), nullable=True, default=0)
    charm_attack_delay = Column(mysql.TINYINT(display_width=3), nullable=True, default=0)
    charm_accuracy_rating = Column(mysql.MEDIUMINT(display_width=9), nullable=True, default=0)
    charm_avoidance_rating = Column(mysql.MEDIUMINT(display_width=9), nullable=True, default=0)
    charm_atk = Column(mysql.MEDIUMINT(display_width=9), nullable=True, default=0)
    skip_global_loot = Column(mysql.TINYINT(display_width=4), nullable=True, default=0)
    rare_spawn = Column(mysql.TINYINT(display_width=4), nullable=True, default=0)
    stuck_behavior = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    model = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    flymode = Column(mysql.TINYINT(display_width=4), nullable=False, default=-1)
    always_aggro = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)
    exp_mod = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)

    alternate_currency = relationship(AlternateCurrency, uselist=False)
    merchantlist = relationship(MerchantList)
    npc_faction = relationship("NPCFaction")
    npc_spells = relationship("NPCSpells")
    spawnentries = relationship(SpawnEntry, back_populates="npc_types", uselist=False)
    npc_emotes = relationship("NPCEmotes", back_populates="npc_emotes")
    npc_types_tint = relationship("NPCTypesTint", back_populates="npc_types_tint", uselist=False)


@mapper_registry.mapped
class Proximities:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/proximities/
    """
    __tablename__ = "proximities"
    zoneid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    exploreid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    minx = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    maxx = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    miny = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    maxy = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    minz = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
    maxz = Column(mysql.FLOAT(14, 6), nullable=False, default=0.000000)
