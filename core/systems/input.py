import pyglet

import esper
from core.components.camera import Camera
from core.components.input import InputState
from core.settings import CAMERA_SPEED


class InputProcessor(esper.Processor):
    def __init__(self, input_entity, camera_entity):
        self.input_entity = input_entity
        self.camera_entity = camera_entity

    def process(self, dt):
        state = esper.component_for_entity(self.input_entity, InputState)
        camera = esper.component_for_entity(self.camera_entity, Camera)

        speed = CAMERA_SPEED * dt

        if pyglet.window.key.W in state.keys_held:
            camera.y += speed
        if pyglet.window.key.S in state.keys_held:
            camera.y -= speed
        if pyglet.window.key.A in state.keys_held:
            camera.x -= speed
        if pyglet.window.key.D in state.keys_held:
            camera.x += speed

        # Clear one-frame states
        state.keys_pressed.clear()
        state.keys_released.clear()

        for screen_x, screen_y in state.mouse_clicks:
            world_x = screen_x + camera.x
            world_y = screen_y + camera.y
            print(
                f"[CLICK] Camera: ({camera.x:.1f}, {camera.y:.1f}) | Cursor (world): ({world_x:.1f}, {world_y:.1f})"
            )

        state.mouse_clicks.clear()
