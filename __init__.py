from sqlalchemy.orm import registry, relationship

mapper_registry = registry()

from .characters import CharacterLanguages
