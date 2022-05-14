from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class AlternateCurrency:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/alternate-currency/alternate_currency/
    """
    __tablename__ = "alternate_currency"
    id = Column(mysql.INTEGER(display_width=10), nullable=False, primary_key=True)
    item_id = Column(mysql.INTEGER(display_width=10), nullable=False)
