from dataclasses import dataclass


@dataclass(slots=True)
class Velocity:
    dx: float
    dy: float


@dataclass(slots=True)
class Position:
    x: float
    y: float
