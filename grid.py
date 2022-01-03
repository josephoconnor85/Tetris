import constants
import shapes
import pygame
from game import Game

pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS",30)


# the grid will be a 10 x 20 matrix, with values initially set to -1 (BLANK) and updated to 0-6 (representing the 7 colours) if filled
# the map list is a matrix of identical size to the grid, containing tuples with x,y co-ordinates of each grid cell

class Grid():
    def __init__(self,win):
        self.win = win
        self.grid = [[-1 for _ in range(constants.GRID_WIDTH)] for _ in range(constants.GRID_HEIGHT)]
        self.map = [[(constants.LEFT + int(constants.BLOCK_SIZE * j),constants.TOP + int(constants.BLOCK_SIZE * i)) for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        self.game = Game()
        

    def draw_grid(self):
        self.win.fill(constants.GRAY)
        self.win.fill(constants.WHITE,(constants.LEFT,constants.TOP,constants.GAME_WIDTH,constants.GAME_HEIGHT))
        self.score_surface = myfont.render(f"Score : {self.game.score}",False,(constants.WHITE))
        self.win.blit(self.score_surface,(500,100))
        self.level_surface = myfont.render(f"Level : {self.game.level}",False,(constants.WHITE))
        self.win.blit(self.level_surface,(500,200))
        self.lines_surface = myfont.render(f"Lines : {self.game.lines}",False,(constants.WHITE))
        self.win.blit(self.lines_surface,(500,300))
        self.hs_surface = myfont.render(f"High Score : {self.game.high_score}",False,(constants.WHITE))
        self.win.blit(self.hs_surface,(500,400))

        
        for i in range(len(self.grid)): # len 20 - y values
            for j in range(len(self.grid[0])): # len 10 - x values
                cell_value = self.grid[i][j]
                if cell_value == int(-1):
                    pass
                else:
                    color = constants.SHAPE_COLORS[shapes.list_colours[cell_value]]
                    coordinates = self.map[i][j]
                    pygame.draw.rect(self.win,color,(coordinates[0],coordinates[1],constants.BLOCK_SIZE,constants.BLOCK_SIZE))

                    

    def check_lines(self):
        count_lines = 0
        i = len(self.grid) - 1
        while i >= 0:
            if -1 not in self.grid[i]:
                del self.grid[i]
                self.grid.insert(0,[-1 for i in range(constants.GRID_WIDTH)])
                count_lines += 1
            else:
                i -= 1
        self.game.increase_points(count_lines)
        self.game.increase_lines(count_lines)
        self.game.increase_level()
            


    def check_game_over(self):
        for cell in self.grid[0]:
            if cell != -1:
                self.game.update_leaderboard()
                return True
        for i in range(3,8):
            if self.grid[1][i] != -1:
                self.game.update_leaderboard()
                return True
