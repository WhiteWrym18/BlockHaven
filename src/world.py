from typing import List, Optional
from blocktype import BlockType  # Import BlockType from blocktype.py

class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Optional[BlockType]]] = []  # 2D grid of BlockType
        self.generate_world()

    def generate_world(self):
        """Generate the world with blocks."""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y < self.height - 5:
                    row.append(BlockType.GRASS)  # Top layers are grass
                elif y < self.height - 1:
                    row.append(BlockType.DIRT)  # Middle layers are dirt
                else:
                    row.append(BlockType.STONE)  # Bottom layers are stone
            self.grid.append(row)
