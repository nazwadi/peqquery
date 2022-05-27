from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from meta import Base


class Books(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/books/books/
    """
    __tablename__ = "books"
    name = Column(mysql.VARCHAR(30), nullable=False, primary_key=True)
    txtfile = Column(mysql.TEXT, nullable=False)  # The text in the book. ` Represents line spaces (13 lines per page)
    language = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
