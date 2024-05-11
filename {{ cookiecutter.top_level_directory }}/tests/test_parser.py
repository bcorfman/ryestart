import os

import pytest

from core.parser import add_border, load_grid


@pytest.mark.unit
def test_load_grid():
    grid_file = os.path.join("data", "grid.txt")
    grid = load_grid(filename=grid_file)
    assert grid[4][14] == "S"


@pytest.mark.unit
def test_add_border():
    grid_file = os.path.join("data", "grid.txt")
    grid = load_grid(filename=grid_file)
    grid = add_border(grid)
    assert grid[5][15] == "S"
