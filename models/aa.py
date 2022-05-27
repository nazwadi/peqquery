from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import mysql

from meta import Base
from .spells import SpellsNew


class AAAbility(Base):
    __tablename__ = "aa_ability"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    """Unique AA Identifier"""
    name = Column(mysql.TEXT, nullable=False)
    """Name"""
    category = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """AA Category (see https://docs.eqemu.io/server/aas/aa-categories)"""
    classes = Column(mysql.INTEGER(display_width=10), nullable=False, default=131070)
    """Classes (see https://docs.eqemu.io/server/player/class-list) Bitmasks"""
    races = Column(mysql.INTEGER(display_width=10), nullable=False, default=65535)
    """Races (see https://docs.eqemu.io/server/npc/race-list)"""
    drakkin_heritage = Column(mysql.INTEGER(display_width=10), nullable=False, default=127)
    """Drakkin Heritage: 127 = All"""
    deities = Column(mysql.INTEGER(display_width=10), nullable=False, default=131071)
    """Deities (see https://docs.eqemu.io/server/player/deity-list)"""
    status = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Minimum Status (see https://docs.eqemu.io/server/player/status-levels)"""
    type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """AA Type (see https://docs.eqemu.io/server/aas/aa-types)"""
    charges = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Number of Charges"""
    grant_only = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Grant Only Flag: 0 = No, 1 = Yes"""
    first_rank_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """First Rank Identifier"""
    enabled = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    """Enabled: 0 = No, 1 = Yes"""
    reset_on_death = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)


class AARanks(Base):
    __tablename__ = "aa_ranks"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(AAAbility.id),
                nullable=False, primary_key=True)
    """AA Identifier (see https://docs.eqemu.io/schema/aas/aa_ability/)"""
    upper_hotkey_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Upper Hotkey SID"""
    lower_hotkey_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Lower Hotkey SID"""
    title_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Title SID"""
    desc_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Description SID"""
    cost = Column(mysql.INTEGER(display_width=10), nullable=False, default=1)
    """Cost in AA Points"""
    level_req = Column(mysql.INTEGER(display_width=10), nullable=False, default=51)
    """Level Required"""
    spell = Column(mysql.INTEGER(display_width=10), ForeignKey(SpellsNew.id),
                   nullable=False, default=-1)
    """Spell Identifier (see https://docs.eqemu.io/schema/spells/spells_new/)"""
    spell_type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Spell Type (see https://docs.eqemu.io/server/spells/spell-types)"""
    recast_time = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Recast Timer"""
    expansion = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Expansion Identifier (see https://docs.eqemu.io/server/operation/expansion-list)"""
    prev_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Previous Rank Identifier"""
    next_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    """Next Rank Identifier"""


class AARankEffects(Base):
    __tablename__ = "aa_rank_effects"
    rank_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(AARanks.id),
                     nullable=False, primary_key=True)
    """Rank Identifier (see https://docs.eqemu.io/schema/aas/aa_ranks/)"""
    slot = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=1)
    """AA Slot"""
    effect_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Spell Effect Identifier (see https://docs.eqemu.io/server/spells/spell-effect-ids)"""
    base1 = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """First Base Value"""
    base2 = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    """Second Base Value"""


class AARankPrereqs(Base):
    __tablename__ = "aa_rank_prereqs"
    rank_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(AARanks.id),
                     nullable=False, primary_key=True)
    """Rank Identifier (see https://docs.eqemu.io/schema/aas/aa_ranks/)"""
    aa_id = Column(mysql.INTEGER(display_width=10), ForeignKey(AAAbility.id),
                   nullable=False, primary_key=True)
    """AA Identifier (see https://docs.eqemu.io/schema/aas/aa_ability/)"""
    points = Column(mysql.INTEGER(display_width=10), nullable=False)
    """Cost in AA Points"""
