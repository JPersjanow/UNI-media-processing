import numpy as np

class GameOfLife:
    def __init__(self):
        self.grid_size = 100
        self.grid = np.zeros((self.grid_size, self.grid_size))

    def print_grid(self):
        self.grid[0][2] = 4
        print(self.grid)
        print(f"type of grid: {type(self.grid)}")

    def check_grid(self):
        for x in range(0, self.grid_size, 1):
            for y in range(0, self.grid_size, 1):
                neighbours = self.check_neighbours(x, y, self.grid)
                
    
    def check_neighbours(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check: list = []
        if self.grid_size > position_x > 0 and self.grid_size > position_y > 0:
            if grid[position_x - 1][position_y] == 1:
                life_check.append(True)
            else:
                life_check.append(False)
            if grid[position_x + 1][position_y] == 1:
                life_check.append(True)
            else:
                life_check(False)
            if grid[position_x][position_y + 1] == 1:
                life_check.append(True)
            else:
                life_check(False)
            if grid[position_x][position_y - 1] == 1:
                life_check.append(True)
            else:
                life_check(False)
        elif position_x == 0 and self.grid_size > position_y > 0:
            

        return life_check 

g = GameOfLife()
g.print_grid()
g.check_grid()
g.print_grid()