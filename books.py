from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Books:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/books/books/
    """
    __tablename__ = "books"
    name = Column(mysql.VARCHAR(30), nullable=False, primary_key=True)
    txtfile = Column(mysql.TEXT, nullable=False)  # The text in the book. ` Represents line spaces (13 lines per page)
    language = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
