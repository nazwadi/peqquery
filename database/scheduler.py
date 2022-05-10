from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class ServerScheduledEvents:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/scheduler/server_scheduled_events/
    """
    __tablename__ = "server_scheduled_events"
    id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None, auto_increment="auto")
    description = Column(mysql.VARCHAR(255), nullable=True, default=None)
    event_type = Column(mysql.VARCHAR(100), nullable=True, default=None)
    event_data = Column(mysql.TEXT, nullable=True, default=None)
    minute_start = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    hour_start = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    day_start = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    month_start = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    year_start = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    minute_end = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    hour_end = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    day_end = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    month_end = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    year_end = Column(mysql.INTEGER(display_width=11), nullable=True, default=0)
    cron_expression = Column(mysql.VARCHAR(100), nullable=True, default=None)
    created_at = Column(mysql.DATETIME, nullable=True, default=None)
    deleted_at = Column(mysql.DATETIME, nullable=True, default=None)
