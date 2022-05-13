from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class NPCEmotes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_emotes/
    """
    __tablename__ = "npc_emotes"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True, default=None, auto_increment="auto")
    emoteid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                     unique=False, primary_key=True, default=0)
    event_ = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    text = Column(mysql.VARCHAR(display_width=512), nullable=False, default=None)


@mapper_registry.mapped
class NPCFaction:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_faction/
    """
    __tablename__ = "npc_faction"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    primaryfaction = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ignore_primary_assist = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)


@mapper_registry.mapped
class NPCFactionEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_faction_entries/
    """
    __tablename__ = "npc_faction_entries"
    npc_faction_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    faction_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    value = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    npc_value = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    temp = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)


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
                primary_key=True, default=None, auto_increment="auto")
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    parent_list = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    attack_proc = Column(mysql.SMALLINT(5), nullable=False, default=-1)
    proc_chance = Column(mysql.TINYINT(display_width=3), nullable=False, default=3)
    range_proc = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    rproc_chance = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    defensive_proc = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    dproc_chance = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    fail_recast = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
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


@mapper_registry.mapped
class NPCSpellsEffects:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_effects/
    """
    __tablename__ = "npc_spells_effects"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, auto_increment="auto")
    name = Column(mysql.TINYTEXT, nullable=True, default=None)
    parent_list = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class NPCSpellsEffectsEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_effects_entries/
    """
    __tablename__ = "npc_spells_effects_entries"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, auto_increment="auto")
    npc_spells_effects_id = Column(mysql.INTEGER(display_width=11, nullable=False,
                                                 unique=False, primary_key=True, default=0))
    spell_effect_id = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=255)
    se_base = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    se_limit = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    se_max = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class NPCSpellsEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_spells_entries/
    """
    __tablename__ = "npc_spells_entries"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False,
                primary_key=True, default=None, auto_increment="auto")
    npc_spells_id = Column(mysql.INTEGER(display_width=11), nullable=False, unique=False, primary_key=True, default=0)
    spellid = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    type = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=255)
    manacost = Column(mysql.SMALLINT(display_width=5), nullable=False, default=-1)
    recast_delay = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    priority = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    resist_adjust = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    min_hp = Column(mysql.SMALLINT(display_width=5), nullable=True, default=0)
    max_hp = Column(mysql.SMALLINT(display_width=5), nullable=True, default=0)


@mapper_registry.mapped
class NPCTypes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/npcs/npc_types/
    """
    __tablename__ = "npc_types"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
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
    #TODO Finish this table


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
