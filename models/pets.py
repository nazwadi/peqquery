from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()


@mapper_registry.mapped
class Pets:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets/
    """
    __tablename__ = "pets"
    id = Column(mysql.INTEGER(display_width=20), nullable=False, primary_key=True, default=None, autoincrement="auto")
    type = Column(mysql.VARCHAR(64), nullable=False, unique=False, primary_key=True)
    petpower = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    npcID = Column(mysql.INTEGER(display_width=11), nullable=False, default=0)
    temp = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    petcontrol = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    petnaming = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    monsterflag = Column(mysql.TINYINT(display_width=4), nullable=False, default=0)
    equipmentset = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)

    npc_types = relationship("NPCTypes", back_populates="pets", uselist=False)


@mapper_registry.mapped
class PetsBeastlordData:
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


@mapper_registry.mapped
class PetsEquipmentSet:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets_equipmentset/
    """
    __tablename__ = "pets_equipmentset"
    set_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    setname = Column(mysql.VARCHAR(30), nullable=False)
    nested_set = Column(mysql.INTEGER(display_width=11), nullable=False, default=-1)

    pets_equipmentset_entries = relationship("PetsEquipmentSetEntries", back_populates="pets_equipmentset")


@mapper_registry.mapped
class PetsEquipmentSetEntries:
    """
    EQEMU Docs URL: https://docs.eqemu.io/schema/pets/pets_equipmentset_entries/
    """
    __tablename__ = "pets_equipmentset_entries"
    set_id = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    slot = Column(mysql.INTEGER(display_width=11), nullable=False, primary_key=True, default=None)
    item_id = Column(mysql.INTEGER(display_width=11), nullable=False, default=None)
