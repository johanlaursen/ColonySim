import arcade

from core.settings import RESOLUTION
from core.views.map_view import MapView

SCREEN_WIDTH, SCREEN_HEIGHT = RESOLUTION
SCREEN_TITLE = "COLONY SIM"


class MainWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.map_view = MapView()
        self.show_view(self.map_view)


if __name__ == "__main__":
    game = MainWindow()
    arcade.run()
