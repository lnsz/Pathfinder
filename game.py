import game_functions as gf
import game_graphics as gg


if __name__ == '__main__':
    WALL = "x"
    SP = "S"  # staring point
    EP = "E"  # ending point
    P = "*"  # path
    N = "o"  # empty space
    window_x = 600
    window_y = 400
    map_file = open("map.txt", 'r')
    mp = gf.generate_map(map_file)
    gf.print_map(mp)
    print()
    window = gg.create_window(window_x, window_y)

    while(True):
        paths = gf.find_paths(mp, gf.starting_point(mp, SP), gf.ending_point(mp, EP), WALL)
        solution = ""
        if gf.is_solvable(paths):
            d_map = gf.distance_map(mp, paths)
            correct_path = gf.generate_path(gf.starting_point(mp, SP), gf.ending_point(mp, EP), d_map)
            solved_map = gf.completed_map(mp, correct_path, SP, EP)
            gf.print_map(solved_map)

            for point in correct_path:
                solution += "x: {0}\ty: {1}\n".format(point["x"], point["y"])
        else:
            solution = "No solution"
        print(solution)
        gg.draw_map(window, solved_map, WALL, SP, EP, P)
        gg.update_map(window, mp, window.getMouse(), WALL, N, gf.starting_point(mp, SP), gf.ending_point(mp, EP))
