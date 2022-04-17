from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Item:
    __tablename__ = "item"

    id = Column(mysql.INTEGER(display_width=11, unsigned=True),
                nullable=False, primary_key=True, autoincrement="auto", default=0)
    minstatus = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    Name = Column(mysql.VARCHAR(64), nullable=False)
    aagi = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ac = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    accuracy = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    acha = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    adex = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    aint = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    artifactflag = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    asta = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    astr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    attack = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augrestrict = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot1type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot1visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot2type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot2visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot3type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot3visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot4type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot4visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot5type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot5visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot6type = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augslot6visible = Column(mysql.TINYINT(display_width=3), nullable=False, default=0)
    augtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    avoidance = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    awis = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bagsize = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bagslots = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bagtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bagwr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    banedmgamt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    banedmgraceamt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    banedmgbody = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    banedmgrace = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bardtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    bardvalue = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    book = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    casttime = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    casttime_ = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    charmfile = Column(mysql.VARCHAR(32), nullable=False)
    charmfileid = Column(mysql.VARCHAR(32), nullable=False)
    classes = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    color = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    combateffects = Column(mysql.VARCHAR(10), nullable=False)
    extradmgskill = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    extradmgamt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    price = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    cr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    damage = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    damageshield = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    deity = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    delay = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augdistiller = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    dotshielding = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    dr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clicktype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clicklevel2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    elemdmgtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    elemdmgamt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    endur = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionamt1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionamt2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionamt3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionamt4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionmod1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionmod2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionmod3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    factionmod4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    filename = Column(mysql.VARCHAR(32), nullable=False)
    focuseffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    fr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    fvnodrop = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    haste = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clicklevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    hp = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    regen = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    icon = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    idfile = Column(mysql.VARCHAR(30), nullable=False)
    itemclass = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    itemtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ldonprice = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ldontheme = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    ldonsold = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    light = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    lore = Column(mysql.VARCHAR(80), nullable=False)
    loregroup = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    magic = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    mana = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    manaregen = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    enduranceregen = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    material = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    herosforgemodel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    maxcharges = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    mr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    nodrop = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    norent = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pendingloreflag = Column(mysql.TINYINT(3, unsigned=True), nullable=False, default=0)
    pr = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procrate = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    races = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    range = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    reclevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    recskill = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    reqlevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    sellrate = Column(mysql.FLOAT, nullable=False, default=0)
    shielding = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    size = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    skillmodtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    skillmodvalue = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    slots = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clickeffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    spellshield = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    strikethrough = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    stunresist = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    summonedflag = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    tradeskills = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    favor = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    weight = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK012 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK013 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    benefitflag = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK054 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK059 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    booktype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    recastdelay = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    recasttype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    guildfavor = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK123 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK124 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    attuneable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    nopet = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    updated = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    comment = Column(mysql.VARCHAR(255), nullable=False)
    UNK127 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    pointtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    potionbelt = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    potionbeltslots = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    stacksize = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    notransfer = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    stackable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK134 = Column(mysql.VARCHAR(255), nullable=False)
    UNK137 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    proceffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    proctype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    proclevel2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    proclevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK142 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    worneffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    worntype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornlevel2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornlevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK147 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focustype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focuslevel2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focuslevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK152 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrolleffect = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrolltype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrolllevel2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrolllevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK157 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    serialized = Column(mysql.DATETIME, nullable=True)
    verified = Column(mysql.DATETIME, nullable=True)
    serialization = Column(mysql.TEXT, nullable=True)
    source = Column(mysql.VARCHAR(20), nullable=False)
    UNK033 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    lorefile = Column(mysql.VARCHAR(32), nullable=False)
    UNK014 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    svcorruption = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    skillmodmax = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK060 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot1unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot2unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot3unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot4unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot5unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    augslot6unk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK120 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK121 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    questitemflag = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK132 = Column(mysql.TEXT, nullable=True)
    clickunk5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clickunk6 = Column(mysql.VARCHAR(32), nullable=False)
    clickunk7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procunk1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procunk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procunk3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procunk4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    procunk6 = Column(mysql.VARCHAR(32), nullable=False)
    procunk7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    wornunk6 = Column(mysql.VARCHAR(32), nullable=False)
    wornunk7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    focusunk6 = Column(mysql.VARCHAR(32), nullable=False)
    focusunk7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk1 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk2 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk3 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk4 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk5 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    scrollunk6 = Column(mysql.VARCHAR(32), nullable=False)
    scrollunk7 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK193 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    purity = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    evoitem = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    evoid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    evolvinglevel = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    evomax = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    clickname = Column(mysql.VARCHAR(64), nullable=False)
    procname = Column(mysql.VARCHAR(64), nullable=False)
    wornname = Column(mysql.VARCHAR(64), nullable=False)
    focusname = Column(mysql.VARCHAR(64), nullable=False)
    scrollname = Column(mysql.VARCHAR(64), nullable=False)
    dsmitigation = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_str = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_int = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_wis = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_agi = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_dex = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_sta = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_cha = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_pr = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_dr = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_fr = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_cr = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_mr = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    heroic_svcorrup = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    healamt = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    spelldmg = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    clairvoyance = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    backstabdmg = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    created = Column(mysql.VARCHAR(64), nullable=False)
    elitematerial = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    ldonsellbackrate = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    scriptfileid = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    expendablearrow = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    powersourcecapacity = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardeffect = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardeffecttype = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardlevel2 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardlevel = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardunk1 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardunk2 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardunk3 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardunk4 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardunk5 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    bardname = Column(mysql.VARCHAR(64), nullable=False)
    bardunk7 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    UNK214 = Column(mysql.SMALLINT(display_width=6), nullable=False, default=0)
    subtype = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK220 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK221 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    heirloom = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK223 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK224 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK225 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK226 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK227 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK228 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK229 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK230 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK231 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK232 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK233 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK234 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    placeable = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK236 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK237 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK238 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK239 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK240 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    UNK241 = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    epicitem = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)


@mapper_registry.mapped
class ItemTick:
    """
    EQEMU Docs URL:  https://docs.eqemu.io/schema/items/item_tick/
    """
    __tablename__ = "item_tick"

    it_itemid = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_chance = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_level = Column(mysql.INTEGER(display_width=11), nullable=False)
    it_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    it_qglobal = Column(mysql.VARCHAR(50), nullable=False)
    it_bagslot = Column(mysql.TINYINT(display_width=4), nullable=False)
