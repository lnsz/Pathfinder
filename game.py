import game_functions as gf
import game_graphics as gg
import grid as gr


if __name__ == '__main__':
    WALL = "x"
    SP = "S"  # staring point
    EP = "E"  # ending point
    PATH = "*"  # path
    EM = "o"  # empty space
    d_move = True  # diagonal movement on/off
    ERROR_MESSAGE = "Not a valid position"
    window_x = 1280
    window_y = 720
    grid_x = 16
    grid_y = 12
    start_pos = (0, grid_y//2)
    end_pos = (grid_x-1, grid_y//2)
    window = gg.create_window(window_x, window_y)
    correct_path = []
    previous_path = []
    grid = gr.Grid(window, grid_x, grid_y, start_pos, end_pos)
    # initial grid
    gg.draw_grid(window, grid)
    while True:
        # find all possible shortest paths
        paths = gf.find_paths(grid, start_pos, end_pos, WALL, d_move)
        # if there are any possible paths

        if gf.is_solvable(paths):
            # create a new grid with the distances
            gf.distance_map(grid, paths)
            # create a list of points that forms the correct path
            correct_path = gf.generate_path(start_pos, end_pos, grid, d_move)
            correct_path.pop(0)
            correct_path.pop(len(correct_path)-1)
            # create a map with solution
            gf.complete_map(grid, correct_path, start_pos, end_pos, SP)
            grid.clean_grid(EM)
        else:
            print(ERROR_MESSAGE, end="")

        gg.update_grid(window, grid, correct_path, previous_path,
                       EM, WALL, PATH)
        print()
        print("Path Length: " + str(len(correct_path)), end="")
        print()
        print()
        gg.create_wall(window, grid, window.getMouse(), WALL, EM,
                       start_pos, end_pos)
        previous_path = correct_path[:]
