from graphics import *


def create_window(x, y):
    """
    (int, int) -> GraphWin object

    Return a GraphWin object with x and y dimensions.
    """

    window = GraphWin('Path Finding Algorithm', x, y)
    return window


def draw_grid(window, grid):
    """
    (GraphWin object, Grid object) -> NoneType

    Draw grid on window.
    """

    for y in grid.get_tiles():
        for tile in y:
            tile.update_colour()
            tile.draw(window)


def update_grid(window, grid, c_path, p_path, empty, wall, path):
    """
    (GraphWin object, Grid object, list of tuple, list of tuple, str, str, str)
    -> NoneType

    Redraw the tiles that changed in the last loop of the main program and
    update the grid object. The tiles to be updated have their coordinates in
    c_path and p_path (current path and previous path) with the first element
    being the x coordinate and the second element the y coordinate. empty, wall
    and path are the characters that represent the value of the tiles.
    """

    for i in p_path:
        if grid.value_at(i[0], i[1]) != wall:
            grid.modify_tile(i[0], i[1], empty)
            grid.tile_at(i[0], i[1]).update_colour()
            grid.tile_at(i[0], i[1]).draw(window)

    for i in c_path:
        grid.modify_tile(i[0], i[1], path)
        grid.tile_at(i[0], i[1]).update_colour()
        grid.tile_at(i[0], i[1]).draw(window)


def create_wall(window, grid, mouse, wall, empty, start, end):
    """
    (GraphWin object, Grid object, mouse position, str, str, tuple, tuple) ->
    NoneType

    Creates or destroys a wall at the mouse position, updates the grid and
    draws to window. The tile at start and end cannot be changed. wall and empty
    are the characters that represent the value of the tiles
    """

    x = int(mouse.x / (window.getWidth() / grid.get_length()))
    y = int(mouse.y / (window.getHeight() / grid.get_height()))
    if (x != start[0] or y != start[1]) and (x != end[0] or y != end[1]):
        if grid.value_at(x, y) == wall:
            print("Wall destroyed at (" + str(x) + ", " + str(y), end=").")
            grid.modify_tile(x, y, empty)
            grid.tile_at(x, y).update_colour()
            grid.tile_at(x, y).draw(window)
        else:
            print("Wall placed at (" + str(x) + ", " + str(y), end="). ")
            grid.modify_tile(x, y, wall)
            grid.tile_at(x, y).update_colour()
            grid.tile_at(x, y).draw(window)

