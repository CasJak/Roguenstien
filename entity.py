from typing import Tuple


class Entity:
    """
    Generic class for all entities (Player, enemies, items, weapons, ammo)
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move entity around using x and y
        self.x += dx
        self.y += dy
