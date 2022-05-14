from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class RuleSets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/rules/rule_sets/
    """
    __tablename__ = "rule_sets"
    ruleset_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False,
                        primary_key=True, default=None, autoincrement="auto")
    name = Column(mysql.VARCHAR(255), nullable=False)

    rule_values = relationship("RuleValues", back_populates="rule_sets")


@mapper_registry.mapped
class RuleValues:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/rules/rule_values/
    """
    __tablename__ = "rule_values"
    ruleset_id = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, primary_key=True, default=0)
    rule_name = Column(mysql.VARCHAR(64), nullable=False, primary_key=True)
    rule_value = Column(mysql.VARCHAR(30), nullable=False)
    notes = Column(mysql.TEXT, nullable=True, default=None)
