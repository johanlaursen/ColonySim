# from pyglet.sprite import Sprite
# from pytmx.util_pyglet import load_pyglet
# from core.components.camera import Camera
# FLIP_HORIZONTAL = 0x80000000
# FLIP_VERTICAL = 0x40000000
# FLIP_DIAGONAL = 0x20000000
# TODO: NOT CURRENTLY USED, KEEPING OUTLINE FOR LATER USE
# class TileMap:
#     def __init__(self, map_file: str):
#         self.tmx_data = load_pyglet(map_file)
#         self.width = self.tmx_data.width
#         self.height = self.tmx_data.height
#         self.tilewidth = self.tmx_data.tilewidth
#         self.tileheight = self.tmx_data.tileheight
#     def get_tile_gid(self, x: int, y: int) -> int:
#         # Assuming single tile layer
#         layer = self.tmx_data.layers[0]
#         return layer.data[y][x]  # pytmx uses [y][x] order
# class TileRenderer:
#     def __init__(self, tilemap: TileMap):
#         self.tilemap = tilemap
#         self.tiles_by_coord: dict[tuple[int, int], tuple[Sprite, int, int]] = {}
#         # {(x, y): (sprite, world_x, world_y)}
#         self._load_tiles()
#     def _load_tiles(self):
#         from pytmx import TiledTileLayer
#         for layer in self.tilemap.tmx_data.visible_layers:
#             if isinstance(layer, TiledTileLayer):
#                 for x, y, gid in layer.iter_data():
#                     if gid == 0:
#                         continue
#                     FLIP_FLAGS = FLIP_DIAGONAL | FLIP_HORIZONTAL | FLIP_VERTICAL
#                     raw_gid = gid & ~FLIP_FLAGS
#                     tile_image = self.tilemap.tmx_data.get_tile_image_by_gid(raw_gid)
#                     if isinstance(tile_image, tuple):
#                         tile_image = tile_image[0]
#                     if tile_image:
#                         world_x = x * self.tilemap.tilewidth
#                         world_y = y * self.tilemap.tileheight
#                         sprite = Sprite(
#                             img=tile_image,
#                             x=world_x,
#                             y=world_y,
#                             batch=None,  # NOT added to a batch!
#                         )
#                         self.tiles_by_coord[(x, y)] = (sprite, world_x, world_y)
#     def draw(self, camera: "Camera", screen_width: int, screen_height: int):
#         tile_w = self.tilemap.tilewidth
#         tile_h = self.tilemap.tileheight
#         start_x = int(camera.x // tile_w)
#         end_x = int((camera.x + screen_width) // tile_w) + 1
#         start_y = int(camera.y // tile_h)
#         end_y = int((camera.y + screen_height) // tile_h) + 1
#         # Clamp to map bounds
#         start_x = max(0, start_x)
#         end_x = min(self.tilemap.width, end_x)
#         start_y = max(0, start_y)
#         end_y = min(self.tilemap.height, end_y)
#         for y in range(start_y, end_y):
#             for x in range(start_x, end_x):
#                 tile = self.tiles_by_coord.get((x, y))
#                 if tile:
#                     sprite, world_x, world_y = tile
#                     sprite.x = world_x - camera.x
#                     sprite.y = world_y - camera.y
#                     sprite.draw()
