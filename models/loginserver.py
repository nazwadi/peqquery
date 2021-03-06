from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import Base


class LoginAccounts(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loginserver/login_accounts/
    """
    __tablename__ = "login_accounts"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=None)
    account_name = Column(mysql.VARCHAR(50), nullable=False, default=None)
    account_password = Column(mysql.TEXT, nullable=False, default=None)
    account_email = Column(mysql.VARCHAR(100), nullable=False, default=None)
    source_loginserver = Column(mysql.VARCHAR(64), nullable=True, unique=False, primary_key=True, default=None)
    last_ip_address = Column(mysql.VARCHAR(80), nullable=False, default=None)
    last_login_date = Column(mysql.DATETIME, nullable=False, default=None)
    created_at = Column(mysql.DATETIME, nullable=True, default=None)
    updated_at = Column(mysql.DATETIME, nullable=True, default="CURRENT_TIMESTAMP")


class LoginApiTokens(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loginserver/login_api_tokens/
    """
    __tablename__ = "login_api_tokens"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, autoincrement="auto")
    token = Column(mysql.VARCHAR(200), nullable=True, default=None)
    can_write = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    can_read = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    created_at = Column(mysql.DATETIME, nullable=True, default=None)
    updated_at = Column(mysql.DATETIME, nullable=True, default="CURRENT_TIMESTAMP")


class LoginServerAdmins(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loginserver/login_server_admins/
    """
    __tablename__ = "login_server_admins"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    account_name = Column(mysql.VARCHAR(30), nullable=False, default=None)
    account_password = Column(mysql.VARCHAR(255), nullable=False, default=None)
    first_name = Column(mysql.VARCHAR(50), nullable=False, default=None)
    last_name = Column(mysql.VARCHAR(50), nullable=False, default=None)
    email = Column(mysql.VARCHAR(100), nullable=False, default=None)
    registration_date = Column(mysql.DATETIME, nullable=False, default=None)
    registration_ip_address = Column(mysql.VARCHAR(80), nullable=False, default=None)


class LoginWorldServers(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/loginserver/login_world_servers/
    """
    __tablename__ = "login_world_servers"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    long_name = Column(mysql.VARCHAR(100), nullable=False, default=None)
    short_name = Column(mysql.VARCHAR(100), nullable=False, default=None)
    tag_description = Column(mysql.VARCHAR(50), nullable=False)
    login_server_list_type_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    last_login_date = Column(mysql.DATETIME, nullable=True, default=None)
    last_ip_address = Column(mysql.VARCHAR(80), nullable=True, default=None)
    login_server_admin_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    is_server_trusted = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    note = Column(mysql.VARCHAR(255), nullable=True, default=None)
