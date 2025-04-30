from dataclasses import dataclass


@dataclass(slots=True)
class InputState:
    keys_held: set
    keys_pressed: set
    keys_released: set
    mouse_clicks: list  # list of (x, y) screen coordinates
