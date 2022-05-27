from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base


class QSMerchantTransactionRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_merchant_transaction_record/
    """
    __tablename__ = "qs_merchant_transaction_record"
    # TODO


class QSMerchantTransactionRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_merchant_transaction_record_entries/
    """
    __tablename__ = "qs_merchant_transaction_record_entries"
    # TODO


class QSPlayerAARateHourly(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_aa_rate_hourly/
    """
    __tablename__ = "qs_player_aa_rate_hourly"
    # TODO


class QSPlayerDeleteRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_delete_record/
    """
    __tablename__ = "qs_player_delete_record"
    # TODO


class QSPlayerDeleteRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_delete_record_entries/
    """
    __tablename__ = "qs_player_delete_record_entries"
    # TODO


class QSPlayerEvents(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_events/
    """
    __tablename__ = "qs_player_events"
    # TODO


class QSPlayerHandinRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_handin_record/
    """
    __tablename__ = "qs_player_handin_record"
    # TODO


class QSPlayerHandinRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_handin_record_entries/
    """
    __tablename__ = "qs_player_handin_record_entries"
    # TODO


class QSPlayerMoveRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_move_record/
    """
    __tablename__ = "qs_player_move_record"
    # TODO


class QSPlayerMoveRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_move_record_entries/
    """
    __tablename__ = "qs_player_move_record_entries"
    # TODO


class QSPlayerNPCKillRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_npc_kill_record/
    """
    __tablename__ = "qs_player_npc_kill_record"
    # TODO


class QSPlayerNPCKillRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_npc_kill_record_entries/
    """
    __tablename__ = "qs_player_npc_kill_record_entries"
    # TODO


class QSPlayerSpeech(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_speech/
    """
    __tablename__ = "qs_player_speech"
    # TODO


class QSPlayerTradeRecord(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_trade_record/
    """
    __tablename__ = "qs_player_trade_record"
    # TODO


class QSPlayerTradeRecordEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/query-server/qs_player_trade_record_entries/
    """
    __tablename__ = "qs_player_trade_record_entries"
    # TODO
