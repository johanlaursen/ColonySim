from dataclasses import dataclass


@dataclass(slots=True)
class Camera:
    x: float = 0.0
    y: float = 0.0
