import numpy as np
import random
import matplotlib.pyplot as plt

class GameOfLife:
    def __init__(self):
        self.grid_size = 100
        self.grid = np.zeros((self.grid_size, self.grid_size))
        self.grid_max_size = self.grid_size - 1

    def simulate(self, number_of_sumulations):
        self.initiate_grid()

        for i in range(0, number_of_sumulations, 1):
            self.check_grid()
            self.save_plot(self.grid, i)


    def initiate_grid(self):
        for ix, iy in np.ndindex(self.grid.shape):
            if random.random() < 0.5:
                self.grid[ix][iy] = 0
            else:
                self.grid[ix][iy] = 1

    def check_grid(self):
        for ix, iy in np.ndindex(self.grid.shape):
            neighbour_list = self.check_neighbours(ix, iy, self.grid)
            if self.decide_if_alive(self.grid[ix][iy], neighbour_list):
                self.grid[ix][iy] = 1
            else:
                self.grid[ix][iy] = 0
                
    def decide_if_alive(self,cell: int, neighbour_list: list) -> bool:
        if cell == 1:
            if neighbour_list.count(True) == 2 or neighbour_list.count(True) == 3:
                return True
            else:
                return False
        elif cell == 0:
            if neighbour_list.count(True) == 3:
                return True
            else:
                return False

    def check_neighbours(self, position_x: int, position_y: int, grid: np.array) -> list:

        if position_y > 0 and position_y < self.grid_max_size and position_x > 0 and position_x < self.grid_max_size:
            return self.check_neighbours_without_border(position_x, position_y, grid)

        elif position_y > 0 and position_y < self.grid_max_size and position_x == 0:
            return self.check_neighbours_when_x_zero(position_x, position_y, grid)

        elif position_y > 0 and position_y < self.grid_max_size and position_x == self.grid_max_size:
            return self.check_neighbours_when_x_max(position_x, position_y, grid)
        
        elif position_y == 0 and position_x > 0 and position_x < self.grid_max_size:
            return self.check_neighbours_when_y_zero(position_x, position_y, grid)

        elif position_y == self.grid_max_size and position_x > 0 and position_x < self.grid_max_size:
            return self.check_neighbours_when_y_max(position_x, position_y, grid)

        elif position_x == 0 and position_y == 0:
            return self.check_left_upper_corner(position_x, position_y, grid)
        
        elif position_x == self.grid_max_size and position_y == 0:
            return self.check_right_upper_corner(position_x, position_y, grid)

        elif position_x == 0 and position_y == self.grid_max_size:
            return self.check_left_lower_corner(position_x, position_y, grid)

        elif position_x == self.grid_max_size and position_y == self.grid_max_size:
            return self.check_right_lower_corner(position_x, position_y, grid)


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

    def check_neighbours_when_x_max(self, position_x: int, position_y: int, grid: np.array) -> list:
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
    
    def check_neighbours_when_y_zero(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []
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
    
    def check_neighbours_when_y_max(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []
        if grid[position_x - 1][position_y] == 1:
            life_check.append(True)
        else:
            life_check.append(False)
        if grid[position_x + 1][position_y] == 1:
            life_check.append(True)
        else:
            life_check.append(False)
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
        return life_check

    def check_left_upper_corner(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []

        if grid[position_x][position_y + 1] == 1:
            life_check.append(True)
        else:
            life_check.append(False)
        if grid[position_x + 1][position_y + 1] == 1:
            life_check.append(True)
        else:
            life_check.append(False)
        if grid[position_x + 1][position_y] == 1:
            life_check.append(True)
        else:
            life_check.append(False)

        return life_check
    
    def check_right_upper_corner(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []

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

        return life_check
    
    def check_left_lower_corner(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []

        if grid[position_x][position_y - 1] == 1:
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

        return life_check
    
    def check_right_lower_corner(self, position_x: int, position_y: int, grid: np.array) -> list:
        life_check = []

        if grid[position_x][position_y - 1] == 1:
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

        return life_check

    def save_plot(self, grid: np.array, iteration: int):
        plt.imshow(grid, cmap='hot')
        plt.colorbar()
        plt.imsave(f'life_{iteration}.png', grid)

if __name__ == '__main__':
    g = GameOfLife()
    g.simulate(10)