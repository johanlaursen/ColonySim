from arcade import Window
from arcade.gui import UIAnchorLayout
from arcade.gui import UIGridLayout
from arcade.gui import UITextureButton
from arcade.gui import UIView

from core.spritemap import SPRITEMAP


class BuildUI(UIAnchorLayout):
    """Build UI for the game.
    Using anchor to define where the UI is placed on the screen
    Will probably refactor this to be a generic "Right UI Panel" and have
     the build UI be a child of that in the future"""

    def __init__(self, window: Window, view: UIView, *args, **kwargs):

        # x,y is the bottom left corner of the UI
        # width, height is the size of the UI
        # Set to be right most 20% of the window
        # x = window.width - window.width * 0.2  # 20% of the screen width
        # y = 0.0 # Bottom of the screen
        # width = window.width * 0.2
        # height = window.height
        # print(x,y,width,height)
        # x=0

        super().__init__(*args, **kwargs)

        # TODO will loop through all buildable entities and create buttons for them
        self.grid = UIGridLayout(
            column_count=2,
            row_count=4,
            horizontal_spacing=20,
            vertical_spacing=20,
        )

        placeable_button_types = ["person", "tree", "fallowed_ground", "tent"]
        placeable_button_types = [
            SPRITEMAP[button] for button in placeable_button_types
        ]

        for c in range(1):
            for r in range(len(placeable_button_types)):
                # button = UIFlatButton(text=f"Button {r * 2 + c + 1}", width=20)
                button = UITextureButton(
                    texture=view.texture_grid[placeable_button_types[r]],
                    width=16,
                    height=16,
                )
                self.grid.add(button, column=c, row=r)

        self.add(self.grid, anchor_x="right", anchor_y="center")
        print(self.grid.children)
