import random

import arcade
from arcade.camera import Camera2D
from arcade.math import Vec2

from core.settings import MAP_TILE_HEIGHT
from core.settings import MAP_TILE_WIDTH
from core.settings import RESOLUTION
from core.settings import SCROLL_ZOOM_SPEED
from core.settings import TILE_SIZE
from core.spritemap import SPRITEMAP

SCREEN_WIDTH, SCREEN_HEIGHT = RESOLUTION
SCREEN_TITLE = "COLONY SIM"


class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # arcade.set_background_color(arcade.color.AMAZON)

        self.sprite_sheet = arcade.SpriteSheet("resources/colored_packed.png")
        self.texture_grid = self.sprite_sheet.get_texture_grid(
            size=(16, 16), columns=49, count=49 * 22
        )

        self.map_width = MAP_TILE_WIDTH
        self.map_height = MAP_TILE_HEIGHT
        self.tile_size = TILE_SIZE
        self.map_sprites = arcade.SpriteList()

        self.ground_types = [
            SPRITEMAP["ground"],
            SPRITEMAP["ground_dirt"],
            SPRITEMAP["ground_dirt_2"],
        ]
        for row in range(self.map_height):
            for col in range(self.map_width):
                ground_type = random.choices(
                    population=self.ground_types, weights=[0.9, 0.09, 0.01], k=1
                )[0]
                sprite = arcade.Sprite()
                sprite.texture = self.texture_grid[ground_type]
                sprite.center_x = col * (self.tile_size)
                sprite.center_y = row * (self.tile_size)
                self.map_sprites.append(sprite)

        self.selection = 0
        self.sprite_list = arcade.SpriteList()

        self.camera = Camera2D()

        self.camera_scale = 1.0
        self.camera_position = Vec2(0, 0)

        self.is_dragging = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.map_sprites.draw()

        # Cycle through the sprite list
        # self.sprite_list.clear()
        # current_sprite = sprite = arcade.Sprite(self.texture_grid[self.selection],1,0, 0)
        # self.sprite_list.append(sprite)
        # self.sprite_list.draw()
        # arcade.draw_text(f"Selected: {self.selection}", 10, 10, arcade.color.WHITE, 14)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y > 0:
            self.camera_scale *= 1 + SCROLL_ZOOM_SPEED
        elif scroll_y < 0:
            self.camera_scale /= 1 + SCROLL_ZOOM_SPEED

        self.camera.zoom = self.camera_scale

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_dragging = True
            self.last_mouse_x = x
            self.last_mouse_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.is_dragging = False

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.is_dragging:
            scale = 1 / self.camera_scale
            movement = Vec2(dx * scale, dy * scale)
            self.camera_position = self.camera_position - movement
            self.camera.position = self.camera_position

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.selection += 1
        elif key == arcade.key.DOWN:
            self.selection -= 1

    def on_update(self, delta_time):
        pass


if __name__ == "__main__":
    game = MainWindow()
    arcade.run()
