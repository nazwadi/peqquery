from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry


@mapper_registry.mapped
class Account:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/account/account/
    """
    __tablename__ = "account"

    id = Column(mysql.INTEGER(display_width=11), primary_key=True, nullable=False, autoincrement="auto")
    """Unique Account Identifier"""
    name = Column(mysql.VARCHAR(30), nullable=False, primary_key=True)
    """Name"""
    charname = Column(mysql.VARCHAR(64), nullable=False)
    """Character name last logged in on this account"""
    sharedplat = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    """Platinum in Shared Bank"""
    password = Column(mysql.VARCHAR(50), nullable=False)
    """Private loginserver password"""
    status = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    """Status (see https://docs.eqemu.io/server/player/status-levels)"""
    ls_id = Column(mysql.VARCHAR(64), nullable=True, primary_key=True, default="eqemu")
    """"""
    lsaccount_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True)
    """Loginserver Account Identifier"""
    gmspeed = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """GM Speed: 0 = Disabled, 1 = Enabled"""
    revoked = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    """OOC Revoked: 0 = False, 1 = True"""
    karma = Column(mysql.INTEGER(display_width=5, unsigned=True), nullable=False, default=0)
    """Karma"""
    minilogin_ip = Column(mysql.VARCHAR(32), nullable=False)
    """Minilogin IP Address"""
    hideme = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Hide Me: 0 = Disabled, 1 = Enabled"""
    rulesflag = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    """Rules Flag"""
    suspendeduntil = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    """Time Suspension of the Account ends"""
    time_creation = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Time Creation UNIX Timestamp"""
    expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Expansion"""
    ban_reason = Column(mysql.TEXT, nullable=True)
    """Ban Reason"""
    suspend_reason = Column(mysql.TEXT, nullable=True)
    """Suspension Reason"""

    account_flags = relationship("AccountFlags", back_populates="account")
    account_rewards = relationship("AccountRewards", back_populates="account")
    sharedbank = relationship("SharedBank", back_populates="account")
    bug_reports = relationship("BugReports", back_populates="account")
    account_ip = relationship("AccountIP", back_populates="account")


@mapper_registry.mapped
class AccountFlags:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/account/account_flags/
    """
    __tablename__ = "account_flags"
    p_accid = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('account.id'),
                     nullable=False, primary_key=True)
    """Account Identifier (see https://docs.eqemu.io/schema/account/account/)"""
    p_flag = Column(mysql.VARCHAR(50), nullable=False, primary_key=True)
    """Name"""
    p_value = Column(mysql.VARCHAR(80), nullable=False)
    """Value"""

    account = relationship("Account", back_populates="account_flags")


@mapper_registry.mapped
class AccountIP:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/account/account_ip/
    """
    __tablename__ = "account_ip"
    accid = Column(mysql.INTEGER(display_width=11), ForeignKey('account.id'),
                   nullable=False, primary_key=True, default=0)
    ip = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    count = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    lastused = Column(mysql.TIMESTAMP, nullable=False, default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    account = relationship("Account", back_populates="account_ip")


@mapper_registry.mapped
class AccountRewards:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/account/account_rewards/
    """
    __tablename__ = "account_rewards"
    account_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('account.id'),
                        nullable=False, primary_key=True)
    reward_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('veteran_reward_templates.reward_id'),
                       nullable=False, primary_key=True)
    amount = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False)

    account = relationship("Account", back_populates="account_rewards")


@mapper_registry.mapped
class SharedBank:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/account/sharedbank/
    """
    __tablename__ = "sharedbank"
    acctid = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey('account.id'),
                    nullable=True, primary_key=True, default=0)
    slotid = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True, default=0)
    charges = Column(mysql.SMALLINT(display_width=3, unsigned=True), nullable=True, default=0)
    augslot1 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot2 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot3 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot4 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot5 = Column(mysql.MEDIUMINT(display_width=7, unsigned=True), nullable=False, default=0)
    augslot6 = Column(mysql.MEDIUMINT(display_width=7), nullable=False, default=0)
    custom_data = Column(mysql.TEXT, nullable=True)

    account = relationship("Account", back_populates="sharedbank")
