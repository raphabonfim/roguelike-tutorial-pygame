class Entity:
    """
    A generic object to represent players, enemies, items, etc
    """

    def __init__(self, x: int, y: int, glyph: str, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.glyph = glyph
        self.color = color

    def move(self, dx: int, dy: int):
        # Move the Entity by a given amount
        self.x += dx
        self.y += dy
