from typing import Tuple


class Entity:
    """
    A generic object to represent platers, enemies, items, potions, etc.
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char  # character char e.g. "@"
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        """Move by entity by a given amount"""
        self.x += dx
        self.y += dy
