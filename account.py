from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Account:
    __tablename__ = "account"

    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, autoincrement="auto")
    name = Column(mysql.VARCHAR(30), nullable=False, primary_key=True)
    charname = Column(mysql.VARCHAR(64), nullable=False)
    sharedplat = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    password = Column(mysql.VARCHAR(50), nullable=False)
    status = Column(mysql.INTEGER(display_width=5), nullable=False, default=0)
    ls_id = Column(mysql.VARCHAR(64), nullable=True, primary_key=True, default="eqemu")
    lsaccount_id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=True)
    gmspeed = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    revoked = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    karma = Column(mysql.INTEGER(display_width=5, unsigned=True), nullable=False, default=0)
    minilogin_ip = Column(mysql.VARCHAR(32), nullable=False)
    hideme = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    rulesflag = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    suspendeduntil = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    time_creation = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    expansion = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    ban_reason = Column(mysql.TEXT, nullable=True)
    suspend_reason = Column(mysql.TEXT, nullable=True)

    account_flags = relationship("AccountFlags", back_populates="account_flags")
    account_rewards = relationship("AccountRewards", back_populates="account_rewards")
    sharedbank = relationship("SharedBank", back_populates="sharedbank")
    bug_reports = relationship("BugReports", back_populates="bug_reports")
    account_ip = relationship("AccountIP", back_populates="account_ip")


@mapper_registry.mapped
class AccountFlags:
    __tablename__ = "account_flags"
    p_accid = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('account.id'),
                     nullable=False, primary_key=True)
    p_flag = Column(mysql.VARCHAR(50), nullable=False, primary_key=True)
    p_value = Column(mysql.VARCHAR(80), nullable=False)


@mapper_registry.mapped
class AccountIP:
    __tablename__ = "account_ip"
    accid = Column(mysql.INTEGER(display_width=11), ForeignKey('account.id'),
                   nullable=False, primary_key=True, default=0)
    ip = Column(mysql.VARCHAR(32), nullable=False, primary_key=True)
    count = Column(mysql.INTEGER(display_width=11), nullable=False, default=1)
    lastused = Column(mysql.TIMESTAMP, nullable=False, default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


@mapper_registry.mapped
class AccountRewards:
    __tablename__ = "account_rewards"
    account_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('account.id'),
                        nullable=False, primary_key=True)
    reward_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey('veteran_reward_templates.reward_id'),
                       nullable=False, primary_key=True)
    amount = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False)


@mapper_registry.mapped
class SharedBank:
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
