from graphics import *


def create_window(x, y):
    win = GraphWin('Path Finding Algorithm', x, y)
    return win


def temp(window):
    a = Point(0, 0)
    a.draw(window)


def draw_solution(window, c_grid, wall, sp, ep, path):
    for y in c_grid.get_tiles():
        for tile in y:
            tile.update_colour()
            tile.get_shape().draw(window)

def cls(window, c_grid, wall, sp, ep, path):
    for y in c_grid.get_tiles():
        for tile in y:
            tile.update_colour()
            tile.get_shape().undraw()


def update_grid(window, grid, mouse, wall, empty, start, end):
    x = mouse.x//(window.getWidth() // grid.get_height())
    y = mouse.y//(window.getHeight() // grid.get_length())
    if (x != start[0] or y != start[1]) and (x != end[0] or y != end[1]):
        if grid.tile_at(x, y) == wall:
            grid.modify_tile(x, y, empty)
        else:
            grid.modify_tile(x, y, wall)
