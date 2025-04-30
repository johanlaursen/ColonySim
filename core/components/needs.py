from dataclasses import dataclass


@dataclass(slots=True)
class Hunger:
    current: float
    max: float = 100.0


@dataclass(slots=True)
class Sleep:
    current: float
    max: float = 100.0
