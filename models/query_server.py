from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from meta import mapper_registry


@mapper_registry.mapped
class QSMerchantTransactionRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_merchant_transaction_record/
    """
    __tablename__ = "qs_merchant_transaction_record"
    # TODO


@mapper_registry.mapped
class QSMerchantTransactionRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_merchant_transaction_record_entries/
    """
    __tablename__ = "qs_merchant_transaction_record_entries"
    # TODO


@mapper_registry.mapped
class QSPlayerAARateHourly:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_aa_rate_hourly/
    """
    __tablename__ = "qs_player_aa_rate_hourly"
    # TODO


@mapper_registry.mapped
class QSPlayerDeleteRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_delete_record/
    """
    __tablename__ = "qs_player_delete_record"
    # TODO


@mapper_registry.mapped
class QSPlayerDeleteRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_delete_record_entries/
    """
    __tablename__ = "qs_player_delete_record_entries"
    # TODO


@mapper_registry.mapped
class QSPlayerEvents:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_events/
    """
    __tablename__ = "qs_player_events"
    # TODO


@mapper_registry.mapped
class QSPlayerHandinRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_handin_record/
    """
    __tablename__ = "qs_player_handin_record"
    # TODO


@mapper_registry.mapped
class QSPlayerHandinRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_handin_record_entries/
    """
    __tablename__ = "qs_player_handin_record_entries"
    # TODO


@mapper_registry.mapped
class QSPlayerMoveRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_move_record/
    """
    __tablename__ = "qs_player_move_record"
    # TODO


@mapper_registry.mapped
class QSPlayerMoveRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_move_record_entries/
    """
    __tablename__ = "qs_player_move_record_entries"
    # TODO


@mapper_registry.mapped
class QSPlayerNPCKillRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_npc_kill_record/
    """
    __tablename__ = "qs_player_npc_kill_record"
    # TODO


@mapper_registry.mapped
class QSPlayerNPCKillRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_npc_kill_record_entries/
    """
    __tablename__ = "qs_player_npc_kill_record_entries"
    # TODO


@mapper_registry.mapped
class QSPlayerSpeech:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_speech/
    """
    __tablename__ = "qs_player_speech"
    # TODO


@mapper_registry.mapped
class QSPlayerTradeRecord:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_trade_record/
    """
    __tablename__ = "qs_player_trade_record"
    # TODO


@mapper_registry.mapped
class QSPlayerTradeRecordEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_trade_record_entries/
    """
    __tablename__ = "qs_player_trade_record_entries"
    # TODO
