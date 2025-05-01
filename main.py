import arcade
from arcade.camera import Camera2D
from arcade.math import Vec2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Camera2D Zoom and Pan"

SCROLL_ZOOM_SPEED = 0.1
PAN_SPEED_DIVISOR = 2


class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.sprite_list = arcade.SpriteList()
        for x in range(0, 2000, 200):
            for y in range(0, 2000, 200):
                sprite = arcade.SpriteCircle(radius=20, color=arcade.color.BLUE)
                sprite.center_x = x
                sprite.center_y = y
                self.sprite_list.append(sprite)

        self.camera = Camera2D()

        self.camera_scale = 1.0
        self.camera_position = Vec2(0, 0)

        self.is_dragging = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.sprite_list.draw()

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

    def on_update(self, delta_time):
        pass


if __name__ == "__main__":
    game = MainWindow()
    arcade.run()
