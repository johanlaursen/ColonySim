from typing import Tuple

from core.components.space import Position
from core.components.space import SpriteComponent
from core.components.space import SpriteListID
from esper import esper


def create_building(
    position: Tuple[float, float],
    sprite_list_id: int,
    texture_id: int,
    rotation: float = 0.0,
) -> int:
    """
    Create a building entity with the given position, sprite list ID, and texture ID.
    """
    position = Position(*position)
    sprite_list_id = SpriteListID(sprite_list_id)
    sprite_component = SpriteComponent(texture_id, rotation)

    return esper.create_entity(
        position,
        sprite_list_id,
        sprite_component,
    )
