from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import mapper_registry


@mapper_registry.mapped
class AAAbility:
    __tablename__ = "aa_ability"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    name = Column(mysql.TEXT, nullable=False)
    category = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    classes = Column(mysql.INTEGER(display_width=10), nullable=False, default=131070)
    races = Column(mysql.INTEGER(display_width=10), nullable=False, default=65535)
    drakkin_heritage = Column(mysql.INTEGER(display_width=10), nullable=False, default=127)
    deities = Column(mysql.INTEGER(display_width=10), nullable=False, default=131071)
    status = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    charges = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    grant_only = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    first_rank_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    enabled = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=1)
    reset_on_death = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)


@mapper_registry.mapped
class AARanks:
    __tablename__ = "aa_ranks"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    upper_hotkey_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    lower_hotkey_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    title_sid = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    desc_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    cost = Column(mysql.INTEGER(display_width=10), nullable=False, default=1)
    level_req = Column(mysql.INTEGER(display_width=10), nullable=False, default=51)
    spell = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    spell_type = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    recast_time = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    expansion = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    prev_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)
    next_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=-1)


@mapper_registry.mapped
class AARankEffects:
    __tablename__ = "aa_rank_effects"
    rank_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    slot = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=1)
    effect_id = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    base1 = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    base2 = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)


@mapper_registry.mapped
class AARankPrereqs:
    __tablename__ = "aa_rank_prereqs"
    rank_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True)
    aa_id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True)
    points = Column(mysql.INTEGER(display_width=10), nullable=False)
