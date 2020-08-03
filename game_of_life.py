import pygame
import time
import sys


class LifeGame:
    def __init__(self, screen_size, cell_size, ded_clr, alv_clr):

        self.screen_size = screen_size
        self.cell_size = cell_size
        self.ded_clr = ded_clr
        self.alv_clr = alv_clr

        print("input file: ")
        string = input()
        path = "input_files/" + string
        self.file = open(path, "r")
        self.data = list(self.file)
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clear()
        pygame.display.flip()

        self.nc = int(Width / self.cell_size)
        self.nr = int(Height / self.cell_size)

        self.old_grid = self.init_grids()
        self.set_grid()

    def init_grids(self):
        rows = [0] * self.nr
        old_grid = [rows] * self.nc

        return old_grid

    def set_grid(self):
        n = len(self.data)
        for i in range(n):
            x, y = str.split(self.data[i], " ")
            self.old_grid[int(x)][int(y)] = 1
        """for i in range(self.nc):
            for j in range(self.nr):
                if value == None:
                    cellvalue = random.choice([0,1])
                else:
                    cellvalue = value
                self.old_grid[i][j] = cellvalue"""

    def clear(self):
        self.screen.fill(self.ded_clr)

    def check_neighbours(self, x, y):
        cnt = 0
        neighbour_cells = [
            (x - 1, y - 1),
            (x - 1, y + 0),
            (x - 1, y + 1),
            (x + 0, y - 1),
            (x + 0, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 0),
            (x + 1, y + 1),
        ]

        for x, y in neighbour_cells:
            if x >= 0 and y >= 0:
                try:
                    cnt += self.old_grid[x][y]
                except:
                    pass
        return cnt

    def update_generation(self):

        self.old_grid = self.init_grids()

        for i in range(self.nc):
            for j in range(self.nr):
                count = self.check_neighbours(i, j)
                if self.old_grid[i][j] == 0:
                    if count == 3:
                        self.new_grid[i][j] = 1
                    else:
                        self.new_grid[i][j] = 0
                else:
                    if count == 2 or count == 3:
                        self.new_grid[i][j] = 1
                    else:
                        self.new_grid[i][j] = 0

        self.old_grid = self.new_grid

    def draw_grid(self):
        self.clear()
        for i in range(self.nc):
            for j in range(self.nr):
                if self.old_grid[i][j] == 1:
                    color = self.alv_clr
                else:
                    color = self.ded_clr
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        i * self.cell_size + self.cell_size,
                        j * self.cell_size + self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    0,
                )
        pygame.display.flip()

    def run(self):
        self.clear()
        pygame.display.flip()

        while True:
            self.eventhandler()
            self.update_generation()
            self.draw_grid()
            time.sleep(0)

    def eventhandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    screen_size = Width, Height = (600, 600)
    cell_size = 10
    ded_clr = 0, 0, 0
    alv_clr = 255, 255, 255

    game = LifeGame(screen_size, cell_size, ded_clr, alv_clr)
    game.run()
