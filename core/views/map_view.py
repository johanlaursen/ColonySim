import random

import arcade.gui
from arcade.camera import Camera2D
from arcade.gui import UIView
from arcade.math import Vec2

import esper.esper as esper
from core.components import space
from core.settings import MAP_TILE_HEIGHT
from core.settings import MAP_TILE_WIDTH
from core.settings import SCROLL_ZOOM_SPEED
from core.settings import TILE_SIZE
from core.spritemap import SPRITEMAP
from core.ui.build_ui import BuildUI
from core.views.menu_view import MenuView


class MapView(UIView):
    def __init__(self):
        super().__init__()
        # Camera setup
        self.camera = Camera2D()
        self.camera_scale = 1.0
        self.camera_position = Vec2(0, 0)
        # GUI camera for UI elements won't scale with zoom level
        # self.ui_camera = Camera2D()

        # Build UI
        self.build_ui = BuildUI(self.window)

        # self.build_section_manager = SectionManager(self)
        # # self.build_section_manager.camera = self.camera
        # self.build_section_manager.add_section(BuildSection(camera=self.ui_camera))
        # # Section will duplicate the on_key_release event if not removed
        # self.build_section_manager.managed_events.remove("on_key_release")
        # self.build_section_manager_enabled = False

        self.map_width = MAP_TILE_WIDTH
        self.map_height = MAP_TILE_HEIGHT
        self.tile_size = TILE_SIZE
        self.map_sprites = arcade.SpriteList()

        # Load the sprite sheet
        self.sprite_sheet = arcade.SpriteSheet("resources/colored_packed.png")
        self.texture_grid = self.sprite_sheet.get_texture_grid(
            size=(16, 16), columns=49, count=49 * 22
        )

        # TODO move to own function and file
        # CREATING BASIC MAP
        self.ground_types = [
            SPRITEMAP["ground"],
            SPRITEMAP["ground_dirt"],
            SPRITEMAP["ground_dirt_2"],
        ]

        # Generate the map
        sprite_id = 0  # For creating entity
        for row in range(self.map_height):
            for col in range(self.map_width):
                ground_type = random.choices(
                    population=self.ground_types, weights=[0.9, 0.09, 0.01], k=1
                )[0]
                sprite = arcade.Sprite()
                sprite.texture = self.texture_grid[ground_type]
                sprite.center_x = col * self.tile_size
                sprite.center_y = row * self.tile_size
                self.map_sprites.append(sprite)

                position = space.Position(col * self.tile_size, row * self.tile_size)
                tile = space.MapTile(ground_type)
                sprite_list_id = space.SpriteListID(sprite_id)
                esper.create_entity(position, tile, sprite_list_id)
                sprite_id += 1
        # STOP CREATING BASIC MAP

        # Dragging state
        self.is_dragging = False
        self.mouse_start_x = 0
        self.mouse_start_y = 0

        switch_menu_button = arcade.gui.UIFlatButton(text="Pause", width=150)

        # Initialise the button with an on_click event.
        @switch_menu_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            menu_view = MenuView(self)
            self.window.show_view(menu_view)

        # Use the anchor to position the button on the screen.
        self.anchor = self.ui.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="left",
            anchor_y="top",
            child=switch_menu_button,
        )

    def on_draw_before_ui(self):
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
            self.is_dragging = False  # Reset dragging state
            self.mouse_start_x = x
            self.mouse_start_y = y

    def on_key_release(self, key, modifiers):
        print("Key released:", key)
        print("ui children", self.ui.children)
        print("anchor", self.anchor)
        if key == arcade.key.B:
            # enabled = self.build_section_manager_enabled
            if self.build_ui in self.ui.children[0]:
                print("Disabling build ui")
                self.ui.remove(self.build_ui)
                # self.build_section_manager.disable()
            else:
                print("Enabling build ui")
                self.ui.add(self.build_ui)
                # self.build_section_manager.enable()
            # self.build_section_manager_enabled = not enabled

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & arcade.MOUSE_BUTTON_LEFT:
            self.is_dragging = True  # Mark as dragging
            scale = 1 / self.camera_scale
            movement = Vec2(dx * scale, dy * scale)
            self.camera_position = self.camera_position - movement
            self.camera.position = self.camera_position

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.is_dragging:
                # Handle mouse click (no dragging occurred)
                print(f"Mouse clicked at ({x}, {y})")
                # Convert screen coordinates to world coordinates
                world_x, world_y, world_z = self.camera.unproject((x, y))
                print(f"World coordinates: ({world_x}, {world_y}, {world_z})")
            else:
                pass
                # print("Mouse drag ended")

    def on_update(self, delta_time):
        pass
