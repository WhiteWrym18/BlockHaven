from typing import List, Optional
from blocktype import BlockType # Import BlockType from blocktype.py

def get_block(grid: List[List[Optional[BlockType]]], x: int, y: int) -> Optional[BlockType]:
    """Return the block at a specific position."""
    if 0 <= x < len (grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return None

def set_block(grid: List[List[Optional[BlockType]]], x: int, y: int, block_type: BlockType):
    """Set a block at a specific position."""
    if 0 <= x < len (grid[0]) and 0 <= y < len(grid):
        grid[y][x] = block_type
