from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from meta import Base
from .npcs import NPCTypes
from .items import Items


class Pets(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets/
    """
    __tablename__ = "pets"
    id = Column(mysql.INTEGER(display_width=20), nullable=False, primary_key=True, default=None, autoincrement="auto")
    type = Column(mysql.VARCHAR(64), ForeignKey(NPCTypes.name),
                  nullable=False, unique=False, primary_key=True)
    """NPC Type Name (see https://docs.eqemu.io/schema/npcs/npc_types/)"""
    petpower = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """Pet Power"""
    npcID = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    """NPC Type Identifier (see https://docs.eqemu.io/schema/npcs/npc_types/)"""
    temp = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Temporary: 0 = False, 1 = True"""
    petcontrol = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Pet Control: 0 = No Control, 1 = No Attack Contro, 2 = Full Control"""
    petnaming = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """
    Pet Naming: 0 = Soandsos Pet, 1 = Soandsos Familiar, 2 = Soandsos Warder, 3 = Random Naming (i.e. Gobaner),
    4 = Keeps name from npc_types table
    """
    monsterflag = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    """Monster Flag: 0 = False, 1 = True"""
    equipmentset = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    """Pet Equipment Set Identifier (see https://docs.eqemu.io/schema/pets/pets_equipmentset/)"""

    npc_types = relationship("NPCTypes", uselist=False)


class PetsBeastlordData(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets_beastlord_data/
    """
    __tablename__ = "pets_beastlord_data"
    player_race = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, primary_key=True, default=1)
    pet_race = Column(mysql.INTEGER(display_width=10, unsigned=True), nullable=False, default=42)
    texture = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    helm_texture = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)
    gender = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=2)
    size_modifier = Column(mysql.FLOAT(unsigned=True), nullable=True, default=1)
    face = Column(mysql.TINYINT(display_width=3, unsigned=True), nullable=False, default=0)


class PetsEquipmentSet(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets_equipmentset/
    """
    __tablename__ = "pets_equipmentset"
    set_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    """Unique Pet Equipment Set Identifier"""
    setname = Column(mysql.VARCHAR(30), nullable=False)
    """Pet Equipment Set Name"""
    nested_set = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)
    """Nested Set Identifier"""

    pets_equipmentset_entries = relationship("PetsEquipmentSetEntries")


class PetsEquipmentSetEntries(Base):
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets_equipmentset_entries/
    """
    __tablename__ = "pets_equipmentset_entries"
    set_id = Column(mysql.INTEGER(display_width=11), ForeignKey(PetsEquipmentSet.set_id),
                    nullable=False, primary_key=True, default=None)
    """Pet Equipment Set Identifier (see https://docs.eqemu.io/schema/pets/pets_equipmentset/)"""
    slot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    """Slot"""
    item_id = Column(mysql.INTEGER(display_width=11), ForeignKey(Items.id),
                     nullable=False, default=None)
    """Item Identifier (see https://docs.eqemu.io/schema/items/items/)"""
