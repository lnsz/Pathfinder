from graphics import *


def create_window(x, y):
    win = GraphWin('Path Finding Algorithm', x, y)
    return win


def temp(window):
    a = Point(0,0)
    a.draw(window)


def draw_map(window, mp, wall, sp, ep, path):
    tile_length = window.getWidth()//len(mp[0])
    tile_height = window.getHeight()//len(mp)
    pos_x = 0
    pos_y = 0
    for y in mp:
        for x in y:
            tile = Rectangle(Point(pos_x, pos_y), Point(pos_x + tile_length, pos_y + tile_height))
            if x == wall:
                tile.setFill("black")
                tile.setOutline("white")
            elif x == path:
                tile.setFill("green")
                tile.setOutline("black")
            elif x == sp:
                tile.setFill("blue")
                tile.setOutline("black")
            elif x == ep:
                tile.setFill("red")
                tile.setOutline("black")
            else:
                tile.setFill("white")
                tile.setOutline("black")
            tile.draw(window)
            pos_x += tile_length
        pos_x = 0
        pos_y += tile_height


def update_map(window, mp, mouse, wall, empty, start, end):
    x = mouse.x//(window.getWidth()//len(mp[0]))
    y = mouse.y//(window.getHeight()//len(mp))
    if (x != start["x"] or y != start["y"]) and (x != end["x"] or y != end["y"]):
        if mp[y][x] == wall:
            mp[y][x] = empty
        else:
            mp[y][x] = wall
