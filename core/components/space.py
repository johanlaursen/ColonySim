from dataclasses import dataclass

from core.settings import TILE_SIZE


@dataclass(slots=True)
class Velocity:
    dx: float
    dy: float


@dataclass(slots=True)
class Position:
    x: float
    y: float

    @property
    def tile(self):
        """
        Returns the center tile coordinates of the position.
        """
        return int(self.x // TILE_SIZE), int(self.y // TILE_SIZE)

    @staticmethod
    def from_tile(tile_x: int, tile_y: int):
        """
        Returns x and y center coordinates of the tile
        """
        return tile_x * TILE_SIZE, tile_y * TILE_SIZE


@dataclass(slots=True)
class MapTile:
    """
    tile_type: key in the sprite map
    """

    tile_type: int


@dataclass(slots=True)
class SpriteListID:
    """
    sprite_list_id: id of the sprite in the sprite list
    """

    sprite_list_id: int
