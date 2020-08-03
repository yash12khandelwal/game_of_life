import pygame
import time
import sys

Screen_Size = Width,Height = (600,600)
Cellsize = 10
Ded_clr = 0,0,0
Alv_clr = 255,255,255

class LifeGame():
    
    def __init__(self):
        string = input()
        path = "input_files/" + string
        self.file = open(path,'r')
        self.data = list(self.file)
        pygame.init()
        self.screen = pygame.display.set_mode(Screen_Size)
        self.clear()
        pygame.display.flip()
        self.init_grids()
        self.set_grid()
        
    def init_grids(self):
        self.nc = int(Width/Cellsize)
        self.nr = int(Height/Cellsize)
        #self.new_grid = [[0 for x in range(self.nr)] * for y in range(self.nc)]
        #self.old_grid = [[0 for x in range(self.nr)] * for y in range(self.nc)]
        self.old_grid = []
        for i in range(self.nc):
            rows = []
            for j in range(self.nr):
                rows.append(0)
            self.old_grid.append(rows)
        
    def set_grid(self):
        n = len(self.data)
        for i in range(n):
            x,y = str.split(self.data[i],' ')
            self.old_grid[int(x)][int(y)] = 1
        '''for i in range(self.nc):
            for j in range(self.nr):
                if value == None:
                    cellvalue = random.choice([0,1])
                else:
                    cellvalue = value
                self.old_grid[i][j] = cellvalue'''   
    
    def clear(self):
        self.screen.fill(Ded_clr)
        
    def check_neighbours(self,x,y):
        cnt=0
        neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                            (x + 0, y - 1),                 (x + 0, y + 1),
                            (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
        
        for x,y in neighbour_cells:
         if x >= 0 and y >= 0:
            try:
                cnt += self.old_grid[x][y]
            except:
                pass
        return cnt
        
    def update_generation(self):
        
        self.new_grid = []
        for i in range(self.nc):
            rows = []
            for j in range(self.nr):
                rows.append(0)
            self.new_grid.append(rows)
        
        for i in range(self.nc):
            for j in range(self.nr):
                count = self.check_neighbours(i,j)
                if self.old_grid[i][j] == 0:
                    if count == 3:
                        self.new_grid[i][j] = 1
                    else:
                        self.new_grid[i][j] = 0
                else:
                    if count==2 or count==3:
                        self.new_grid[i][j] =1
                    else:
                        self.new_grid[i][j] =0
                        
        self.old_grid = self.new_grid
                
        
    def draw_grid(self):
        self.clear()
        for i in range(self.nc):
            for j in range(self.nr):
                if self.old_grid[i][j] == 1:
                    color = Alv_clr
                else:
                    color = Ded_clr
                pygame.draw.rect(self.screen,color,(i*Cellsize+Cellsize,j*Cellsize+Cellsize,
                                                     Cellsize,Cellsize),0)
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






if __name__ == '__main__':
    game = LifeGame()
    game.run()