from typing import List, Optional
from blocktype import BlockType  # Import BlockType from blocktype.py
from grid_utils import get_block, set_block # Import utility functions 

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
            
    def get_block(self, x: int, y: init) -> Optional[BlockType]:
        return get_block(self.grid, x, y)
    
    def set_block(self, x: int, y: init, block_type: BlockType):
        set_block(self.grid, x, y, block_type)