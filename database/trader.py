from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Trader:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/trader/trader/
    """
    __tablename__ = "trader"
    char_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    item_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    serialnumber = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    charges = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    item_cost = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    slot_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)


@mapper_registry.mapped
class TraderAudit:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/trader/trader_audit/
    """
    __tablename__ = "trader_audit"
    time = Column(mysql.DATETIME, nullable=False, default="0000-00-00 00:00:00")
    seller = Column(mysql.VARCHAR(64), nullable=False)
    buyer = Column(mysql.VARCHAR(64), nullable=False)
    itemname = Column(mysql.VARCHAR(64), nullable=False)
    quantity = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    totalcost = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    trantype = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
