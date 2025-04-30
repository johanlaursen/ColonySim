import esper
from core.components.space import Position
from core.components.space import Velocity


class MovementSystem:
    def __init__(self):
        super().__init__()

    def process(self, dt):
        # This will iterate over every Entity that has BOTH of these components:
        for ent, (vel, pos) in esper.get_components(Velocity, Position):

            new_x = pos.x + vel.dx
            new_y = pos.y + vel.dy
            pos.x = new_x
            pos.y = new_y
