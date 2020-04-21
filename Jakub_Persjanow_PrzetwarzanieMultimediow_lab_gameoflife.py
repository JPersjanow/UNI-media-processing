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
        with open("grid.txt", "w+") as file:
            for ix, iy in np.ndindex(self.grid.shape):
                if self.grid_size - 1> ix > 0 and self.grid_size - 1 > iy > 0:
                    file.writelines(f"{ix} : {iy}\n")
                
    
    def check_neighbours(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check: list = []

        if position_y > 0 and position_y < self.grid_size and position_x > 0 and position_x < self.grid_size:
            return self.check_neighbours_without_border(position_x, position_y, grid)

        elif position_y > 0 and position_y < self.grid_size and position_x == 0:
            return self.check_neighbours_when_x_zero(position_x, position_y, grid)

        elif position_y > 0 and position_y < self.grid_size and position_x == self.grid_size:
            return self.check_neighbours_when_x_max(position_x, position_y, grid)
        
        elif 
        return life_check

def check_neighbours_without_border(self, position_x: int, position_y: int, grid: np.array) -> list:
    life_check = []
    if grid[position_x - 1][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x - 1][position_y] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x - 1][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    return life_check

def check_neighbours_when_x_zero(self, position_x: int, position_y:int, grid: np.array) -> list:
    life_check = []
    if grid[position_x][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x + 1][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    return life_check

def check_neighbours_when_x_max(self, position_x: int, position_y:int, grid: np.array) -> list:
    life_check = []
    if grid[position_x][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x - 1][position_y - 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x - 1][position_y] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    if grid[position_x - 1][position_y + 1] == 1:
        life_check.append(True)
    else:
        life_check.append(False)
    return life_check

g = GameOfLife()
g.print_grid()
g.check_grid()
# g.print_grid()