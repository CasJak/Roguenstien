from typing import Tuple

import numpy as np

# Define title gfx that are compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

# Struct for holding that data for each tile
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if tile is walkable
        ("transparent", np.bool),  # True if tile doesnt block FOV
        ("dark", graphic_dt),  # Gfx for tiles that are in the "FOG"
    ]
)


def new_tile(
        *,  # Enforce the use of keywords, so that parameter order doesn't matter
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord("░"), (100, 100, 100), (0, 0, 0)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("▓"), (200, 200, 200), (0, 0, 0)),
)
