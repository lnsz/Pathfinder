def find_paths(grid, start, end, wall):
    """
    (Grid object, tuple, tuple, str) -> list of tuple

    Going from the end until start, return all possible paths through the grid
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
    (Grid object, tuple, list of tuple, str) -> list of tuple

    Return all adjacent tiles that are not a wall and not already in the queue
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


def generate_path(start, end, grid):
    """
    (tuple, tuple, Grid object) -> list of tuple

    Return the shortest path from start to end through the grid
    """

    path = [start]
    point = start
    while point != end:
        point = next_point(point, grid)
        path.append(point)
    return path


def next_point(point, grid):
    """
    (tuple, Grid object) -> tuple

    Return an adjacent point in grid with a counter that is exactly 1 less
    than current point
    """

    # if point is not outside map and the adjacent point's counter is 1 less
    # than it's counter
    x = point[0]
    y = point[1]
    if y - 1 >= 0 and grid.value_at(x, y - 1) == grid.value_at(x, y) - 1:
        return (x, y - 1)

    elif x + 1 < grid.get_length() and grid.value_at(x + 1, y) == grid.value_at(x, y) - 1:
        return (x + 1, y)

    elif x - 1 >= 0 and grid.value_at(x - 1, y) == grid.value_at(x, y) - 1:
        return (x - 1, y)

    elif y + 1 < grid.get_height() and grid.value_at(x, y + 1) == grid.value_at(x, y) - 1:
        return (x, y + 1)


def complete_map(grid, solution, start, end, path):
    """
    (Grid object, list of tuple, str, str) -> NoneType

    Change grid to contain the solution for the shortest path from start to end
    """

    for point in solution:
        # if tile is not a start or end tile
        grid.modify_tile(point[0], point[1], path)
