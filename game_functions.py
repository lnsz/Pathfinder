def find_paths(grid, start, end, wall):
    """
    (grid object, tuple, tuple, str) -> list of tuple

    Going from the end until start, find all possible paths through the grid
    avoiding wall, and add them to queue

    """

    # create queue with only endpoint
    # queue is a list of tuples with 3 elements
    # each element is in form(position x, position y, counter)
    # counter tracks how many steps it takes to reach from end
    queue = [(end[0], end[1], 0)]
    for item in queue:
        if item[0] != start[0] or item[1] != start[1]:
            queue.extend(process_adjacent(grid, item, queue, wall))
        else:
            return queue


def process_adjacent(grid, point, queue, wall):
    """
    (grid object, tuple, list of tuple, str) -> list of tuple
    """

    adjacent_points = []
    x = point[0]
    y = point[1]
    c = point[2]
    # if point is not outside grid and is not a wall and does not exist in queue
    if x + 1 < grid.get_length() and grid.value_at(x + 1, y) != wall and \
            duplicate_check(x + 1, y, c + 1, queue):
        adjacent_points.append((x + 1, y, c + 1))

    if x - 1 >= 0 and grid.value_at(x - 1, y) != wall and \
            duplicate_check(x - 1, y, c + 1, queue):
        adjacent_points.append((x - 1, y, c + 1))

    if y + 1 < grid.get_height() and grid.value_at(x, y + 1) != wall and \
            duplicate_check(x, y + 1, c + 1, queue):
        adjacent_points.append((x, y + 1, c + 1))

    if y - 1 >= 0 and grid.value_at(x, y - 1) != wall and \
            duplicate_check(x, y - 1, c + 1, queue):
        adjacent_points.append((x, y - 1, c + 1))
    return adjacent_points


def duplicate_check(x, y, counter, queue):
    """
    (int, int, int, list of tuple) -> bool
    """
    for item in queue:
        if item[0] == x and item[1] == y and item[2] <= counter:
            return False
    return True


def is_solvable(queue):
    """
    (list of tuple) -> bool
    """

    return queue is not None


def distance_map(d_grid, paths):
    """
    (grid object, list of tuple) -> NoneType
    """

    for point in paths:
        d_grid.modify_tile(point[0], point[1], point[2])


def generate_path(start, end, d_map):
    """
    (tuple, tuple, grid object) -> list of tuple
    """

    path = [start]
    point = start
    while point != end:
        point = next_point(point, d_map)
        path.append(point)
    return path


def next_point(point, d_grid):
    """
    (tuple, grid object) -> tuple
    """

    # if point is not outside map and the adjacent point's counter is 1 less
    # than it's counter
    x = point[0]
    y = point[1]
    if y - 1 >= 0 and d_grid.value_at(x, y - 1) == d_grid.value_at(x, y) - 1:
        return (x, y - 1)

    elif x + 1 < d_grid.get_length() and d_grid.value_at(x + 1, y) == d_grid.value_at(x, y) - 1:
        return (x + 1, y)

    elif x - 1 >= 0 and d_grid.value_at(x - 1, y) == d_grid.value_at(x, y) - 1:
        return (x - 1, y)

    elif y + 1 < d_grid.get_height() and d_grid.value_at(x, y + 1) == d_grid.value_at(x, y) - 1:
        return (x, y + 1)


def complete_map(c_grid, solution, start, end, path):
    """
    (grid object, list of tuple, str, str) -> NoneType
    """

    for point in solution:
        # if tile is not a start or end tile
        c_grid.modify_tile(point[0], point[1], path)
