import math

def find_paths(grid, start, end, wall, d_move):
    """
    (Grid object, tuple, tuple, str, bool) -> list of tuple

    Going from the end until start, return all possible paths through the grid
    avoiding wall, and add them to queue. d_move enables or disables diagonal
    movement
    """

    # create queue with only endpoint
    # queue is a list of tuples with 3 elements
    # each element is in form(position x, position y, counter)
    # counter tracks how many steps it takes to reach from end
    queue = [(end[0], end[1], 0)]
    for item in queue:
        if item[0] != start[0] or item[1] != start[1]:
            queue.extend(process_adjacent(grid, item, queue, wall, d_move))
        else:
            return queue


def process_adjacent(grid, point, queue, wall, d_move):
    """
    (Grid object, tuple, list of tuple, str, bool) -> list of tuple

    Return all adjacent tiles that are not a wall and not already in the queue
    """

    adjacent_points = []
    x = point[0]
    y = point[1]
    c = point[2]
    # if point is not outside grid and is not a wall and does not exist in queue
    # right (x + 1)
    if x + 1 < grid.get_length() and grid.value_at(x + 1, y) != wall and \
            duplicate_check(x + 1, y, c + 1, queue):
        adjacent_points.append((x + 1, y, c + 1))
    # left (x - 1)
    if x - 1 >= 0 and grid.value_at(x - 1, y) != wall and \
            duplicate_check(x - 1, y, c + 1, queue):
        adjacent_points.append((x - 1, y, c + 1))
    # down (y + 1)
    if y + 1 < grid.get_height() and grid.value_at(x, y + 1) != wall and \
            duplicate_check(x, y + 1, c + 1, queue):
        adjacent_points.append((x, y + 1, c + 1))
    # up (y - 1)
    if y - 1 >= 0 and grid.value_at(x, y - 1) != wall and \
            duplicate_check(x, y - 1, c + 1, queue):
        adjacent_points.append((x, y - 1, c + 1))
    # d_move enables the other 4 directions
    if d_move:
        # up right (x + 1, y - 1)
        if x + 1 < grid.get_length() and y - 1 >= 0 and grid.value_at(x + 1, y - 1)\
                != wall and duplicate_check(x + 1, y - 1, c + math.sqrt(2), queue):
            adjacent_points.append((x + 1, y - 1, c + math.sqrt(2)))
        # down right (x + 1, y + 1)
        if x + 1 < grid.get_length() and y + 1 < grid.get_height() and grid.value_at(x + 1, y + 1)\
                != wall and duplicate_check(x + 1, y + 1, c + math.sqrt(2), queue):
            adjacent_points.append((x + 1, y + 1, c + math.sqrt(2)))
        # up left (x - 1, y - 1)
        if x - 1 >= 0 and y - 1 >= 0 and grid.value_at(x - 1, y - 1)\
                != wall and duplicate_check(x - 1, y - 1, c + math.sqrt(2), queue):
            adjacent_points.append((x - 1, y - 1, c + math.sqrt(2)))
        # down left (x - 1, y + 1)
        if x - 1 >= 0 and y + 1 < grid.get_height() and grid.value_at(x - 1, y + 1)\
                != wall and duplicate_check(x - 1, y + 1, c + math.sqrt(2), queue):
            adjacent_points.append((x - 1, y + 1, c + math.sqrt(2)))

    return adjacent_points


def duplicate_check(x, y, counter, queue):
    """
    (int, int, int, list of tuple) -> bool

    Return true if and only if queue does not contain an item with the same
    x, y and a lower or equal counter
    """

    for item in queue:
        if item[0] == x and item[1] == y and item[2] <= counter:
            return False
    return True


def is_solvable(paths):
    """
    (list of tuple) -> bool

    Return true if and only if paths contains at least one item (at least one
    path exists)
    """

    return paths is not None


def distance_map(grid, paths):
    """
    (Grid object, list of tuple) -> NoneType

    Replace empty tiles from grid with the number of moves to get there
    """

    for point in paths:
        grid.modify_tile(point[0], point[1], point[2])


def generate_path(start, end, grid, d_move):
    """
    (tuple, tuple, Grid object, bool) -> list of tuple

    Return the shortest path from start to end through the grid
    """

    path = [start]
    point = start
    while point != end:
        point = next_point(point, grid, d_move)
        path.append(point)
    return path


def next_point(point, grid, d_move):
    """
    (tuple, Grid object, bool) -> tuple

    Return an adjacent point with the smallest counter
    """

    # if point is not outside map and the adjacent point's counter is 1 less
    # than it's counter
    x = point[0]
    y = point[1]
    available_spaces = []
    available_points = []
    min_value = math.inf
    current_min = -1
    if x - 1 >= 0:
        available_spaces.append(grid.value_at(x - 1, y))
        available_points.append((x - 1, y))
        if d_move:
            if y - 1 >= 0:
                available_spaces.append(grid.value_at(x - 1, y - 1))
                available_points.append((x - 1, y - 1))
            if y + 1 < grid.get_height():
                available_spaces.append(grid.value_at(x - 1, y + 1))
                available_points.append((x - 1, y + 1))
    if x + 1 < grid.get_length():
        available_spaces.append(grid.value_at(x + 1, y))
        available_points.append((x + 1, y))
        if d_move:
            if y - 1 >= 0:
                available_spaces.append(grid.value_at(x + 1, y - 1))
                available_points.append((x + 1, y - 1))
            if y + 1 < grid.get_height():
                available_spaces.append(grid.value_at(x + 1, y + 1))
                available_points.append((x + 1, y + 1))
    if y - 1 >= 0:
        available_spaces.append(grid.value_at(x, y - 1))
        available_points.append((x, y - 1))
    if y + 1 < grid.get_height():
        available_spaces.append(grid.value_at(x, y + 1))
        available_points.append((x, y + 1))

    for i in range(len(available_spaces)):
        if type(available_spaces[i]) != str and available_spaces[i] < min_value:
            min_value = available_spaces[i]
            current_min = i

    if current_min >= 0:
        return available_points[current_min]


def complete_map(grid, solution, start, end, path):
    """
    (Grid object, list of tuple, str, str) -> NoneType

    Change grid to contain the solution for the shortest path from start to end
    """

    for point in solution:
        # if tile is not a start or end tile
        grid.modify_tile(point[0], point[1], path)
