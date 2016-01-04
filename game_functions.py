import copy


def generate_map(map_file):
    """
    text file open for reading -> list of list of char
    """

    mp = map_file.read().split("\n")
    for i in range(len(mp)):
        mp[i] = list(mp[i])
    return mp


def starting_point(mp, sp):
    """
    list of list of char -> dict of {str:int}
    """

    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x] == sp:
                return {"y": y, "x": x}

    #return {"y": len(mp)-1, "x": len(mp[0])//2}


def ending_point(mp, ep):
    """
    list of list of char -> dict of {str:int}
    """

    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x] == ep:
                return {"y": y, "x": x}


def find_paths(mp, origin, endpoint, wall):
    """
    list of list of char, dict of {str:int}, dict of {str:int} ->
    list of dict of {str:int}
    """

    queue = [{"x": endpoint["x"], "y": endpoint["y"], "counter": 0}]
    for item in queue:
        if item["x"] != origin["x"] or item["y"] != origin["y"]:
            queue.extend(process_adjacent(mp, item, queue, wall))
        else:
            return queue


def distance_map(mp, queue):
    """
    list of list of char, list of dict of {str:int} -> list of list of char
    """

    temp_map = copy.deepcopy(mp)
    for item in queue:
        temp_map[item["y"]][item["x"]] = item["counter"]
    return temp_map


def completed_map(mp, solution, sp, ep):
    """
    list of list of char, list of dict of {str:int} -> list of list of char
    """

    temp_map = copy.deepcopy(mp)
    for point in solution:
        if temp_map[point["y"]][point["x"]] != sp and temp_map[point["y"]][point["x"]] != ep:
         temp_map[point["y"]][point["x"]] = "*"
    return temp_map


def generate_path(origin, endpoint, d_map):
    """
    dict of {str:int}, list of list of char -> dict of {str:int}
    """

    path = [origin]
    point = origin
    while point != endpoint:
        point = next_point(point, d_map)
        path.append(point)
    return path


def next_point(point, d_map):
    """
    dict of {str:int}, list of list of char -> dict of {str:int}
    """

    # if point is not outside map and the adjacent point's counter is 1 less
    # than it's counter
    y = point["y"]
    x = point["x"]
    if y-1 >= 0 and d_map[y-1][x] == d_map[y][x]-1:
        return {"x": x, "y": y-1}

    elif x+1 < len(d_map[y]) and d_map[y][x+1] == d_map[y][x]-1:
        return {"x": x+1, "y": y}

    elif x-1 >= 0 and d_map[y][x-1] == d_map[y][x]-1:
        return {"x": x-1, "y": y}

    elif y + 1 < len(d_map) and d_map[y+1][x] == d_map[y][x]-1:
        return {"x": x, "y": y+1}

def process_adjacent(map, point, queue, wall):
    """
    list of list of char, dict of {str:int}, list of dict of {str:int} ->
    list of dict of {str:int}
    """

    adjacent_points = []
    y = point["y"]
    x = point["x"]
    c = point["counter"]
    # if point is not outside map and is not a wall and does not exist in queue
    if x+1 < len(map[y]) and map[y][x+1] != wall and duplicate_check(x+1, y, c+1, queue):
        adjacent_points.append({"x": x+1, "y": y, "counter": c+1})

    if x-1 >= 0 and map[y][x-1] != wall and duplicate_check(x-1, y, c+1, queue):
        adjacent_points.append({"x": x-1, "y": y, "counter": c+1})

    if y+1 < len(map) and map[y+1][x] != wall and duplicate_check(x, y+1, c+1, queue):
        adjacent_points.append({"x": x, "y": y+1, "counter": c+1})

    if y-1 >= 0 and map[y-1][x] != wall and duplicate_check(x, y-1, c+1, queue):
        adjacent_points.append({"x": x, "y": y-1, "counter": c+1})
    return adjacent_points


def duplicate_check(x, y, counter, queue):
    """
    dict of {str:int}, list of dict of {str:int} -> bool
    """
    for item in queue:
        if item["x"] == x and item["y"] == y and item["counter"] <= counter:
            return False
    return True


def is_solvable(queue):
    """
    list of dict of {str:int} -> bool
    """

    return queue is not None


def print_map(mp):
    """
    list of list of char -> NoneType
    """

    for i in mp:
        for l in i:
            print(str(l), end="\t")
        print("")
        print("")
