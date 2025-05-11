from typing import List, Optional
from blocktype import BlockType  # Import BlockType from blocktype.py

class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Optional[BlockType]]] = []  # 2D grid of BlockType
        self.generate_world()

    def generate_world(self):
        """Generate the world grid with blocks."""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Assign block types based on the row (similar to the original logic)
                if y < self.height - 5:
                    row.append(BlockType.GRASS)  # Top rows are grass
                elif y < self.height - 1:
                    row.append(BlockType.DIRT)  # Middle rows are dirt
                else:
                    row.append(BlockType.STONE)  # Bottom rows are stone
            self.grid.append(row)

    def get_block(self, x: int, y: int) -> Optional[BlockType]:
        """Return the block at a specific position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def set_block(self, x: int, y: int, block_type: BlockType):
        """Set a block at a specific position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = block_type