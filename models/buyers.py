from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class Buyer:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/buyers/buyer/#schema
    """
    __tablename__ = "buyer"
    charid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    buyslot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    itemname = Column(mysql.VARCHAR(65), nullable=False)
    quantity = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    price = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
