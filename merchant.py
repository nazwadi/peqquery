from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class MerchantList:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/merchants/merchantlist/
    """
    __tablename__ = "merchantlist"
    merchantid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    slot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)
    item = Column(mysql.INTEGER(display_width=11, unsigned=True), ForeignKey('items.id'),
                  nullable=False, primary_key=True, unique=False, autoincrement="auto", default=0)
    faction_required = Column(mysql.SMALLINT(display_width=6), nullable=False, default=-100)
    level_required = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    alt_currency_cost = Column(mysql.SMALLINT(display_width=5, unsigned=True), nullable=False, default=0)
    classes_required = Column(mysql.INTEGER(display_width=11), nullable=False, default=65535)
    probability = Column(mysql.INTEGER(display_width=3), nullable=False, default=100)
    min_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    max_expansion = Column(mysql.TINYINT(display_width=4, unsigned=True), nullable=False, default=0)
    content_flags = Column(mysql.VARCHAR(100), nullable=True)
    content_flags_disabled = Column(mysql.VARCHAR(100), nullable=True)

    items = relationship("Item", back_populates="item")


@mapper_registry.mapped
class MerchantListTemp:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/merchants/merchantlist_temp/
    """
    __tablename__ = "merchantlist_temp"

    npcid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    slot = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    itemid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    charges = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=1)
