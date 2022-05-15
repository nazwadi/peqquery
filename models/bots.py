from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from meta import mapper_registry


@mapper_registry.mapped
class BotBuffs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_buffs/
    """
    __tablename__ = "bot_buffs"
    # TODO


@mapper_registry.mapped
class BotData:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_data/
    """
    __tablename__ = "bot_data"
    # TODO


@mapper_registry.mapped
class BotGroups:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_groups/
    """
    __tablename__ = "bot_groups"
    # TODO


@mapper_registry.mapped
class BotGroupMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_group_members/
    """
    __tablename__ = "bot_group_members"
    # TODO


@mapper_registry.mapped
class BotHealRotations:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_heal_rotations/
    """
    __tablename__ = "bot_heal_rotations"
    # TODO


@mapper_registry.mapped
class BotHealRotationMembers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_heal_rotation_members/
    """
    __tablename__ = "bot_heal_rotation_members"
    # TODO


@mapper_registry.mapped
class BotHealRotationTargets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_heal_rotation_targets/
    """
    __tablename__ = "bot_heal_rotation_targets"
    # TODO


@mapper_registry.mapped
class BotInspectMessages:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_inspect_messages/
    """
    __tablename__ = "bot_inspect_messages"
    # TODO


@mapper_registry.mapped
class BotInspectMessages:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_inventories/
    """
    __tablename__ = "bot_inventories"
    # TODO


@mapper_registry.mapped
class BotOwnerOptions:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_owner_options/
    """
    __tablename__ = "bot_owner_options"
    # TODO


@mapper_registry.mapped
class BotPets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_pets/
    """
    __tablename__ = "bot_pets"
    # TODO


@mapper_registry.mapped
class BotPetBuffs:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_pet_buffs/
    """
    __tablename__ = "bot_pet_buffs"
    # TODO


@mapper_registry.mapped
class BotPetInventories:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_pet_inventories/
    """
    __tablename__ = "bot_pet_inventories"
    # TODO


@mapper_registry.mapped
class BotSpellsEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_spells_entries/
    """
    __tablename__ = "bot_spells_entries"
    # TODO


@mapper_registry.mapped
class BotSpellCastingChances:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_spell_casting_chances/
    """
    __tablename__ = "bot_spell_casting_chances"
    # TODO


@mapper_registry.mapped
class BotStances:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_stances/
    """
    __tablename__ = "bot_stances"
    # TODO


@mapper_registry.mapped
class BotTimers:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/bots/bot_timers/
    """
    __tablename__ = "bot_timers"
    # TODO
