from graphics import *


def create_window(x, y):
    win = GraphWin('Path Finding Algorithm', x, y)
    return win


def temp(window):
    a = Point(0, 0)
    a.draw(window)


def draw_grid(window, c_grid):
    for y in c_grid.get_tiles():
        for tile in y:
            tile.update_colour()
            tile.draw(window)


def update_grid(window, grid, c_path, p_path, empty, wall, path):
    for i in p_path:
        if grid.value_at(i[0], i[1]) != wall:
            grid.modify_tile(i[0], i[1], empty)
            grid.tile_at(i[0], i[1]).update_colour()
            grid.tile_at(i[0], i[1]).draw(window)

    for i in c_path:
        grid.modify_tile(i[0], i[1], path)
        grid.tile_at(i[0], i[1]).update_colour()
        grid.tile_at(i[0], i[1]).draw(window)


def create_wall(window, grid, mouse,  wall, empty, start, end):
    x = mouse.x // (window.getWidth() // grid.get_height())
    y = mouse.y // (window.getHeight() // grid.get_length())
    if (x != start[0] or y != start[1]) and (x != end[0] or y != end[1]):
        if grid.value_at(x, y) == wall:
            grid.modify_tile(x, y, empty)
            grid.tile_at(x, y).update_colour()
            grid.tile_at(x, y).draw(window)
        else:
            grid.modify_tile(x, y, wall)
            grid.tile_at(x, y).update_colour()
            grid.tile_at(x, y).draw(window)

