from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import Base


class Guilds(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/guilds/guilds/
    """
    __tablename__ = "guilds"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    name = Column(mysql.VARCHAR(32), nullable=False, unique=True)
    leader = Column(mysql.INTEGER(display_width=11), nullable=False, unique=True, default=0)
    minstatus = Column(mysql.SMALLINT(display_width=5), nullable=False, default=0)
    motd = Column(mysql.TEXT, nullable=False, default=None)
    tribute = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    motd_setter = Column(mysql.VARCHAR(64), nullable=False)
    channel = Column(mysql.VARCHAR(128), nullable=False)
    url = Column(mysql.VARCHAR(512), nullable=False)


class GuildBank(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/guilds/guild_bank/
    """
    __tablename__ = "guild_bank"
    guildid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                     unique=False, primary_key=True, default=0)
    area = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False,
                  unique=False, primary_key=True, default=0)
    slot = Column(mysql.INTEGER(display_width=4, unsigned=True), nullable=False,
                  unique=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    qty = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    donator = Column(mysql.VARCHAR(64), nullable=True, default=None)
    permissions = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    whofor = Column(mysql.VARCHAR(64), nullable=True, default=None)


class GuildRanks(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/guilds/guild_ranks/
    """
    __tablename__ = "guild_ranks"
    guild_id = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, primary_key=True, default=0)
    rank = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    title = Column(mysql.VARCHAR(128), nullable=False)
    can_hear = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_speak = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_invite = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_remove = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_promote = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_demote = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_motd = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    can_warpeace = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


class GuildMembers(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/guilds/guild_members/
    """
    __tablename__ = "guild_members"
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    guild_id = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, default=0)
    rank = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    tribute_enable = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    total_tribute = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    last_tribute = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    banker = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    public_note = Column(mysql.TEXT, nullable=False, default=None)
    alt = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


class GuildRelations(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/guilds/guild_relations/
    """
    __tablename__ = "guild_relations"
    guild1 = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, primary_key=True, default=0)
    guild2 = Column(mysql.MEDIUMINT(display_width=8, unsigned=True), nullable=False, primary_key=True, default=0)
    relation = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
