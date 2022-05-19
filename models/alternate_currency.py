from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql

from meta import mapper_registry


@mapper_registry.mapped
class AlternateCurrency:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/alternate-currency/alternate_currency/
    """
    __tablename__ = "alternate_currency"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True)
    """Alternate Currency Identifier (see https://docs.eqemu.io/server/items/alternate-currencies)"""
    item_id = Column(mysql.INTEGER(display_width=10), ForeignKey("Items.id"),
                     nullable=False)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
