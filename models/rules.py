from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base


class RuleSets(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/rules/rule_sets/
    """
    __tablename__ = "rule_sets"
    ruleset_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False,
                        primary_key=True, default=None, autoincrement="auto")
    """Unique Rule Set Identifier"""
    name = Column(mysql.VARCHAR(255), nullable=False)
    """Name"""

    rule_values = relationship("RuleValues")
    """Relationship Type: Has-Many, Local Key: ruleset_id, Relates to Table: rule_values, Foreign Key: ruleset_id"""


class RuleValues(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/rules/rule_values/
    """
    __tablename__ = "rule_values"
    ruleset_id = Column(mysql.TINYINT(display_width=3, unsigned=True), ForeignKey(RuleSets.ruleset_id),
                        nullable=False, primary_key=True, default=0)
    """Rule Set Identifier (see https://docs.eqemu.io/schema/rules/rule_sets/)"""
    rule_name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    """Rule Name"""
    rule_value = Column(mysql.VARCHAR(30), nullable=False)
    """Rule Value"""
    notes = Column(mysql.TEXT, nullable=True, default=None)
    """Notes"""
