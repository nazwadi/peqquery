from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
class CompletedSharedTaskActivityState:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/completed_shared_task_activity_state/
    """
    __tablename__ = "completed_shared_task_activity_state"
    shared_task_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    activity_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    done_count = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    updated_time = Column(mysql.DATETIME, nullable=False, default=None)
    completed_time = Column(mysql.DATETIME, nullable=False, default=None)


@mapper_registry.mapped
class CompletedSharedTaskMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/completed_shared_task_members/
    """
    __tablename__ = "completed_shared_task_members"
    shared_task_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    character_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    is_leader = Column(mysql.TINYINT(display_width=4), nullable=True, default=None)


@mapper_registry.mapped
class CompletedSharedTasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/completed_shared_tasks/
    """
    __tablename__ = "completed_shared_tasks"
    id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    task_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
    accepted_time = Column(mysql.DATETIME, nullable=True, default=None)
    expire_time = Column(mysql.DATETIME, nullable=True, default=None)
    completion_time = Column(mysql.DATETIME, nullable=True, default=None)
    is_locked = Column(mysql.TINYINT(display_width=1), nullable=True, default=None)


@mapper_registry.mapped
class CompletedTasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/completed_tasks/
    """
    __tablename__ = "completed_tasks"
    charid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    completedtime = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    activityid = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=0)


@mapper_registry.mapped
class GoalLists:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/goallists/
    """
    __tablename__ = "goallists"
    listid = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                    primary_key=True, default=0)
    entry = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                   primary_key=True, default=0)


@mapper_registry.mapped
class SharedTaskActivityState:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/shared_task_activity_state/
    """
    __tablename__ = "shared_task_activity_state"
    shared_task_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    activity_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    done_count = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    updated_time = Column(mysql.DATETIME, nullable=True, default=None)
    completed_time = Column(mysql.DATETIME, nullable=True, default=None)


@mapper_registry.mapped
class SharedTaskDynamicZones:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/shared_task_dynamic_zones/
    """
    __tablename__ = "shared_task_dynamic_zones"
    shared_task_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    dynamic_zone_id = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False,
                             primary_key=True, default=None)


@mapper_registry.mapped
class SharedTaskMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/shared_task_members/
    """
    __tablename__ = "shared_task_members"
    shared_task_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    character_id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None)
    is_leader = Column(mysql.TINYINT(display_width=4), nullable=True, default=None)


@mapper_registry.mapped
class SharedTasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/shared_tasks/
    """
    __tablename__ = "shared_tasks"
    id = Column(mysql.BIGINT(display_width=20), nullable=False, primary_key=True, default=None, autoincrement="auto")
    task_id = Column(mysql.INTEGER(display_width=11), nullable=True, default=None)
    accepted_time = Column(mysql.DATETIME, nullable=True, default=None)
    expire_time = Column(mysql.DATETIME, nullable=True, default=None)
    completion_time = Column(mysql.DATETIME, nullable=True, default=None)
    is_locked = Column(mysql.TINYINT(display_width=1), nullable=True, default=None)


@mapper_registry.mapped
class TaskActivities:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/task_activities/
    """
    __tablename__ = "task_activities"
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    activityid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    step = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    activitytype = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    target_name = Column(mysql.VARCHAR(64), nullable=False)
    item_list = Column(mysql.VARCHAR(128), nullable=False)
    skill_list = Column(mysql.VARCHAR(64), nullable=False, default=-1)
    spell_list = Column(mysql.VARCHAR(64), nullable=False, default=0)
    description_override = Column(mysql.VARCHAR(128), nullable=False)
    goalid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    goalmethod = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    goalcount = Column(mysql.INTEGER(display_width=11), nullable=True, default=1)
    delivertonpc = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    zones = Column(mysql.VARCHAR(64), nullable=False)
    optional = Column(mysql.TINYINT(display_width=1), nullable=False, default=0)


@mapper_registry.mapped
class Tasks:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/tasks/
    """
    __tablename__ = "tasks"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    type = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    duration = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    duration_code = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    title = Column(mysql.VARCHAR(100), nullable=False)
    description = Column(mysql.TEXT, nullable=False, default=None)
    reward = Column(mysql.VARCHAR(64), nullable=False)
    rewardid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    cashreward = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, default=0)
    xpreward = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    rewardmethod = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=2)
    reward_radiant_crystals = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    reward_ebon_crystals = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    minlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    maxlevel = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    level_spread = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    min_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    max_players = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    repeatable = Column(mysql.TINYINT(display_width=1, unsigned=True), nullable=False, default=0)
    faction_reward = Column(mysql.INTEGER(display_width=10), nullable=False, default=0)
    completion_emote = Column(mysql.VARCHAR(512), nullable=False)
    replay_timer_seconds = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)
    request_timer_seconds = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=0)


@mapper_registry.mapped
class TaskSets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/tasks/tasksets/
    """
    __tablename__ = "tasksets"
    id = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
    taskid = Column(mysql.INTEGER(display_width=11, unsigned=True), nullable=False, primary_key=True, default=0)
