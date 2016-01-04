import game_functions as gf
import game_graphics as gg
import grid as gr
import copy


if __name__ == '__main__':
    WALL = "x"
    SP = "S"  # staring point
    EP = "E"  # ending point
    P = "*"  # path
    N = "o"  # empty space
    window_x = 800
    window_y = 600
    grid_x = 15
    grid_y = 15
    start_pos = (0, grid_y-1)
    end_pos = (grid_x-1, 0)
    window = gg.create_window(window_x, window_y)
    grid = gr.Grid(window, grid_x, grid_y, start_pos, end_pos)



    while True:
        # new grid that contains distances instead of tiles
        d_grid = copy.deepcopy(grid)
        # new grid with solution
        c_grid = copy.deepcopy(grid)
        # find all possible shortest paths
        paths = gf.find_paths(grid, start_pos, end_pos, WALL)
        # if there are any possible paths
        if gf.is_solvable(paths):
            # create a new grid with the distances
            gf.distance_map(d_grid, paths)
            # create a list of points that forms the correct path
            correct_path = gf.generate_path(start_pos, end_pos, d_grid)
            # create a map with solution
            gf.complete_map(c_grid, correct_path, SP, EP, P)
        gg.cls(window, c_grid, WALL, SP, EP, P)
        gg.draw_solution(window, c_grid, WALL, SP, EP, P)
        gg.update_grid(window, grid, window.getMouse(), WALL, N, start_pos, end_pos)
        del c_grid
        del d_grid
