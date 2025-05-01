import esper
from core.components.input import InputState


class InputProcessor:
    def __init__(self, input_entity):
        self.input_entity = input_entity

    def process(self, dt):
        esper.component_for_entity(self.input_entity, InputState)
