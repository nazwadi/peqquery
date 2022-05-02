from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class Titles:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/titles/titles/
    """
    __tablename__ = "titles"
    id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                primary_key=True, default=None, autoincrement="auto")
    skill_id = Column(mysql.TINYINT(display_width=3), nullable=False, default=-1)
    min_skill_value = Column(mysql.MEDIUMINT(display_width=8), nullable=False, default=-1)
    max_skill_value = Column(mysql.MEDIUMINT(display_width=8), nullable=False, default=-1)
    min_aa_points = Column(mysql.MEDIUMINT(display_width=8), nullable=False, default=-1)
    max_aa_points = Column(mysql.MEDIUMINT(display_width=8), nullable=False, default=-1)
    _class = Column("class", mysql.TINYINT(display_width=4), nullable=False, default=-1)
    gender = Column(mysql.TINYINT(display_width=1), nullable=False, default=-1)
    char_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    status = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    prefix = Column(mysql.VARCHAR(32), nullable=False)
    suffix = Column(mysql.VARCHAR(32), nullable=False)
    title_set = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
