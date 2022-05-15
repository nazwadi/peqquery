from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .npcs import NPCTypes


@mapper_registry.mapped
class BlockedSpells:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/blocked_spells/
    """
    __tablename__ = "blocked_spells"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    """Unique Blocked Spells Identifier"""
    spellid = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    """Spell Identifier"""
    type = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Blocked Spell Type"""
    zoneid = Column(mysql.INTEGER(display_width=4), nullable=False, default=0)
    """Zone Identifier"""
    x = Column(mysql.FLOAT, nullable=False, default=0)
    """X Coordinate"""
    y = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Coordinate"""
    z = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Coordinate"""
    x_diff = Column(mysql.FLOAT, nullable=False, default=0)
    """X Radius"""
    y_diff = Column(mysql.FLOAT, nullable=False, default=0)
    """Y Radius"""
    z_diff = Column(mysql.FLOAT, nullable=False, default=0)
    """Z Radius"""
    message = Column(mysql.VARCHAR(255), nullable=False, default='')
    """Message when blocked"""
    description = Column(mysql.VARCHAR(255), nullable=False, default='')
    """Blocked spells description"""


@mapper_registry.mapped
class DamageShieldTypes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/damageshieldtypes/
    """
    __tablename__ = "damageshieldtypes"
    spellid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    """Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    type = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """Damage Shield Type (see https://docs.eqemu.io/server/spells/damage-shield-types)"""


@mapper_registry.mapped
class SpellBuckets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/spell_buckets/
    """
    __tablename__ = "spell_buckets"
    spellid = Column(mysql.BIGINT(display_width=11, unsigned=True), nullable=False, primary_key=True, default=None)
    """Unique Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    key = Column(mysql.VARCHAR(100), nullable=True, unique=False, primary_key=True, default=None)
    """Data Bucket Name (see https://docs.eqemu.io/schema/data-storage/data_buckets/)"""
    value = Column(mysql.TEXT, nullable=True, default=None)
    """Data Bucket Value"""


@mapper_registry.mapped
class SpellGlobals:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/spell_globals/
    """
    __tablename__ = "spell_globals"
    spellid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    """Unique Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    spell_name = Column(mysql.VARCHAR(64), nullable=False, default="")
    """Spell Name (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    qglobal = Column(mysql.VARCHAR(65), nullable=False, default="")
    """Quest Global Name (see https://docs.eqemu.io/schema/data-storage/quest_globals/)"""
    value = Column(mysql.VARCHAR(65), nullable=False, default="")
    """Quest Global Value"""


@mapper_registry.mapped
class SpellsNew:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/spells_new/
    """
    __tablename__ = "spells_new"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    name = Column(mysql.VARCHAR(64), nullable=True, default=None)
    player_1 = Column(mysql.VARCHAR(64), nullable=True, default='BLUE_TRAIL')
    teleport_zone = Column(mysql.VARCHAR(64), nullable=True, default=None)
    you_cast = Column(mysql.VARCHAR(120), nullable=True, default=None)
    other_casts = Column(mysql.VARCHAR(120), nullable=True, default=None)
    cast_on_you = Column(mysql.VARCHAR(120), nullable=True, default=None)
    cast_on_other = Column(mysql.VARCHAR(120), nullable=True, default=None)
    spell_fades = Column(mysql.VARCHAR(120), nullable=True, default=None)
    range = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    aoerange = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pushback = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pushup = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    cast_time = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    recovery_time = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    recast_time = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    buffdurationformula = Column(mysql.INTEGER(display_width=11), nullable=False, default=7)
    buffduration = Column(mysql.INTEGER(display_width=11), nullable=False, default=65)
    AEDuration = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    effect_base_value2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_base_value12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effect_limit_value12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    max12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    icon = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    memicon = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    components1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    components2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    components3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    components4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    component_counts1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    component_counts2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    component_counts3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    component_counts4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    NoexpendReagent1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    NoexpendReagent2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    NoexpendReagent3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    NoexpendReagent4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    formula1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    formula12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    LightType = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    goodEffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    Activated = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    resisttype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    effectid1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    effectid12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=254)
    targettype = Column(mysql.INTEGER(display_width=11), nullable=False, default=2)
    basediff = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    skill = Column(mysql.INTEGER(display_width=11), nullable=False, default=98)
    zonetype = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    EnvironmentType = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    TimeOfDay = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    classes1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes13 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes14 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes15 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    classes16 = Column(mysql.INTEGER(display_width=11), nullable=False, default=255)
    CastingAnim = Column(mysql.INTEGER(display_width=11), nullable=False, default=44)
    TargetAnim = Column(mysql.INTEGER(display_width=11), nullable=False, default=13)
    TravelType = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    SpellAffectIndex = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    disallow_sit = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities6 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities8 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities9 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities10 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities11 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities12 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities13 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities14 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities15 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deities16 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field142 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    field143 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    new_icon = Column(mysql.INTEGER(display_width=11), nullable=False, default=161)
    spellanim = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    uninterruptable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ResistDiff = Column(mysql.INTEGER(display_width=11), nullable=False, default=-150)
    dot_stacking_exempt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deleteable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    RecourseLink = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    no_partial_resist = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field152 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field153 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    short_buff_box = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    descnum = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    typedescnum = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    effectdescnum = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    effectdescnum2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    npc_no_los = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field160 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    reflectable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bonushate = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field163 = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    field164 = Column(mysql.INTEGER(display_width=11), nullable=False, default=-150)
    ldon_trap = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    EndurCost = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    EndurTimerIndex = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    IsDiscipline = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field169 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field170 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field171 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field172 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    HateAdded = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    EndurUpkeep = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    numhitstype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    numhits = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pvpresistbase = Column(mysql.INTEGER(display_width=11), nullable=False, default=-150)
    pvpresistcalc = Column(mysql.INTEGER(display_width=11), nullable=False, default=100)
    pvpresistcap = Column(mysql.INTEGER(display_width=11), nullable=False, default=-150)
    spell_category = Column(mysql.INTEGER(display_width=11), nullable=False, default=-99)
    pvp_duration = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pvp_duration_cap = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pcnpc_only_flag = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    cast_not_standing = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    can_mgb = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    nodispell = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    npc_category = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    npc_usefulness = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    MinResist = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    MaxResist = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    viral_targets = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    viral_timer = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    nimbuseffect = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    ConeStartAngle = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ConeStopAngle = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    sneaking = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    not_extendable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field198 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field199 = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    suspendable = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    viral_range = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    songcap = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field203 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field204 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    no_block = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field206 = Column(mysql.INTEGER(display_width=11), nullable=True, default=-1)
    spellgroup = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    rank = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field209 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field210 = Column(mysql.INTEGER(display_width=11), nullable=True, default=1)
    CastRestriction = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    allowrest = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    InCombat = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    OutofCombat = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field215 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field216 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field217 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    aemaxtargets = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    maxtargets = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field220 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field221 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field222 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field223 = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    persistdeath = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    field225 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field226 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    min_dist = Column(mysql.FLOAT, nullable=False, default=0)
    min_dist_mod = Column(mysql.FLOAT, nullable=False, default=0)
    max_dist = Column(mysql.FLOAT, nullable=False, default=0)
    max_dist_mod = Column(mysql.FLOAT, nullable=False, default=0)
    min_range = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field232 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field233 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field234 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field235 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    field236 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)

    auras = relationship("Auras", back_populates="spells_new", uselist=False)
    damageshieldtypes = relationship("DamageShieldTypes", back_populates="spells_new")
    spell_buckets = relationship("SpellBuckets", back_populates="spells_new")
    spell_globals = relationship("SpellGlobals", back_populates="spells_new")
    blocked_spells = relationship("BlockedSpells", back_populates="spells_new")


@mapper_registry.mapped
class Auras:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/spells/auras/
    """
    __tablename__ = "auras"
    type = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None)
    """Unique Aura Identifier"""
    npc_type = Column(mysql.INTEGER(display_width=10), ForeignKey(NPCTypes.id),
                      nullable=False, default=None)
    """NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/)"""
    name = Column(mysql.VARCHAR(64), nullable=False, default=None)
    """Name"""
    spell_id = Column(mysql.INTEGER(display_width=10), ForeignKey(SpellsNew.id), nullable=False, default=None)
    """Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    distance = Column(mysql.INTEGER(display_width=10), nullable=False, default=60)
    """Distance"""
    aura_type = Column(mysql.INTEGER(display_width=10), nullable=False, default=1)
    """Aura Type (see https://docs.eqemu.io/server/spells/aura-types)"""
    spawn_type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Aura Spawn Type (see https://docs.eqemu.io/server/spells/aura-spawn-types)"""
    movement = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Aura Movement Type (see https://docs.eqemu.io/server/spells/aura-movement-types)"""
    duration = Column(mysql.INTEGER(display_width=10), nullable=False, default=5400)
    """Duration"""
    icon = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Icon"""
    cast_time = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Cast Time"""

    npc_types = relationship("NPCTypes", back_populates="auras", uselist=False)
    """Relationship Type: One-to-One, Local Key: npc_type, Relates to Table: npc_types, Foreign Key: id"""
    spells_new = relationship("SpellsNew", back_populates="auras", uselist=False)
    """Relationship Type: One-to-One, Local Key: spell_id, Relates to Table: spells_new, Foreign Key: id"""
