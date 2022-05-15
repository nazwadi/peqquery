from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import mapper_registry
from .items import Items


@mapper_registry.mapped
class Tributes:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tributes/tributes/
    """
    __tablename__ = "tributes"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    unknown = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    name = Column(mysql.VARCHAR(255), nullable=False)
    descr = Column(mysql.MEDIUMTEXT, nullable=False, default=None)
    isguild = Column(mysql.TINYINT(display_width=4), nullable=False, primary_key=True, default=0)  # 0 = False, 1 = True


@mapper_registry.mapped
class TributeLevels:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tributes/tribute_levels/
    """
    __tablename__ = "tribute_levels"
    tribute_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(Tributes.id), primary_key=True,
                        nullable=False, default=0)
    """Unique Tribute Identifier (see https://docs.eqemu.io/schema/tributes/tributes/)"""
    level = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=0)
    """Level"""
    cost = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    """Cost"""
    item_id = Column(mysql.INTEGER(display_width=10, unsigned=True), ForeignKey(Items.id),
                     nullable=False, default=0)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
