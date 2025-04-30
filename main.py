import logging

logging.getLogger("pytmx").setLevel(logging.CRITICAL)

import pyglet
from core.components.camera import Camera
from core.systems.input import InputProcessor
import esper
from core.components.input import InputState
from core.settings import FPS, RESOLUTION
from core.tilemap.tilemap import TileMap, TileRenderer

# Create a basic window
window = pyglet.window.Window(
    width=RESOLUTION[0], height=RESOLUTION[1], caption="Colony Engine"
)


# Add the system
# esper.add_processor(MovementSystem())

# Add a single test entity
# player = esper.create_entity()
# esper.add_component(player, Position(100, 100))
# esper.add_component(player, Velocity(0, 0))


################################################
#  Set up pyglet events for input and rendering:
################################################
@window.event
def on_key_press(symbol, modifiers):
    state = esper.component_for_entity(input_entity, InputState)
    state.keys_held.add(symbol)
    state.keys_pressed.add(symbol)


@window.event
def on_key_release(symbol, modifiers):
    state = esper.component_for_entity(input_entity, InputState)
    state.keys_held.discard(symbol)
    state.keys_released.add(symbol)


@window.event
def on_mouse_press(x, y, button, modifiers):
    state = esper.component_for_entity(input_entity, InputState)
    state.mouse_clicks.append((x, y))


batch = pyglet.graphics.Batch()
tilemap = TileMap("tiled/map_small_32.tmx")
tile_renderer = TileRenderer(tilemap)
camera_entity = esper.create_entity(Camera(x=3459.0, y=3310.6))

input_entity = esper.create_entity(
    InputState(
        keys_held=set(), keys_pressed=set(), keys_released=set(), mouse_clicks=[]
    )
)
input_processor = InputProcessor(input_entity, camera_entity)
esper.add_processor(input_processor)


@window.event
def on_draw():
    window.clear()
    camera = esper.component_for_entity(camera_entity, Camera)
    tile_renderer.draw(camera, window.width, window.height)

    batch.draw()

    # for ent, pos in esper.get_component(Position):
    #     pyglet.shapes.Circle(pos.x, pos.y, 10, color=(255, 100, 100)).draw()


def update(dt):
    esper.process(dt)


# Schedule the update function
pyglet.clock.schedule_interval(update, 1 / FPS)

# Start the game loop
pyglet.app.run()
