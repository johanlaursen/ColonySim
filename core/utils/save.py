import json
from dataclasses import fields
from dataclasses import is_dataclass

import arcade

import esper.esper as esper
from core.components import space

SAVE_LOCATION = "saves/"


def serialize_dataclass(component):
    if is_dataclass(component):
        return {
            field.name: getattr(component, field.name) for field in fields(component)
        }


def save_game(window, filename):
    filename = SAVE_LOCATION + filename

    # Try using __class__.__name__ to get class name instead of hardcoding

    map_tiles = {}
    for ent, (pos, maptile, sprite_list_id) in esper.get_components(
        space.Position, space.MapTile, space.SpriteListID
    ):
        map_tiles[ent] = {
            "position": serialize_dataclass(pos),
            "map_tile": serialize_dataclass(maptile),
            "sprite_list_id": serialize_dataclass(sprite_list_id),
        }
    with open(filename, "w") as f:
        json.dump(map_tiles, f, indent=4)


def load_game(window, filename):
    map_tiles = json.load(open(filename, "r"))
    for ent, (pos, maptile, sprite_list_id) in map_tiles.items():
        pos = space.Position(**pos)
        maptile = space.MapTile(**maptile)
        sprite_list_id = space.SpriteListID(**sprite_list_id)

        esper.create_entity(pos, maptile, sprite_list_id)

        sprite = arcade.Sprite()
        sprite.texture = window.texture_grid[maptile.tile_type]
        sprite.center_x = pos.x
        sprite.center_y = pos.y
        window.map_sprites.append(sprite)
