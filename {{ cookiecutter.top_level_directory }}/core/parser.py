MAX_GRID_WIDTH = 55


def load_grid(**kwargs):
    grid = []
    with open(kwargs["filename"], encoding="utf-8") as gf:
        for line in gf.readlines():
            grid.append(line.rstrip())
    return grid


def add_border(grid):
    new_grid = [MAX_GRID_WIDTH * " "]
    for line in grid:
        new_grid.append(line.ljust(MAX_GRID_WIDTH - 1, " ").rjust(MAX_GRID_WIDTH, " "))
    new_grid.append(MAX_GRID_WIDTH * " ")
    return new_grid
