import pygame
import shapes
import constants
import random


class Tetris():
    def __init__(self,win,grid):
        
        self.win = win
        self.grid = grid
        self.shape = "o"
        self.color = constants.BLACK
        self.map = []
        self.rotation_map = []
        self.rotation = 0

        # set gridx and gridy positions. This is the grid square of the top left hand corner of the 5 x 5 box containing the shape
        self.gridx = constants.START_X
        self.gridy = constants.START_Y
        

        self.left = 100
        self.top = 100
        self.width = 20
        self.height = 20

        self.block_list = []
        self.new_shape()

    def move_down(self):
        self.gridy += 1
        self.grid.draw_grid()
        self.update_shape_position()


    def move_right(self):
        self.gridx += 1
        self.grid.draw_grid()
        self.update_shape_position()

    def move_left(self):
        self.gridx -= 1
        self.grid.draw_grid()
        self.update_shape_position()


    def rotate(self):
        if self.rotation == len(shapes.shapes[self.shape])-1:
            self.rotation = 0
        else:
            self.rotation += 1
        self.rotation_map = self.map[self.rotation]
        self.update_shape_position()
        
        

    def new_shape(self):
        self.shape = random.choice(shapes.list_shapes) # this returns a string name for shape - eg: "s", "l", "o"
        self.color = shapes.list_colours[shapes.list_shapes.index(self.shape)] # updates the self.color for the object
        self.map = shapes.shapes[self.shape] # updates shape map for object
        self.rotation_map = self.map[self.rotation]
        self.update_shape_position()
        for i in range(constants.BLOCKS_PER_SHAPE):
            base_x = self.gridx
            base_y = self.gridy
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]
            coordinates = self.map_coordinates(offset_x,offset_y)
            col = constants.SHAPE_COLORS[self.color]
            block = pygame.draw.rect(self.win,col,(coordinates[0],coordinates[1],constants.BLOCK_SIZE,constants.BLOCK_SIZE))
            self.block_list.append(block)

# the following functions check if the shape can move - down, left, right, or can rotate, without colliding with sides, or other pieces

    def can_move_down(self):
        for i in range(len(self.block_list)):
            base_x = self.gridx
            base_y = self.gridy + 1
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]

            if offset_y not in range(constants.GRID_HEIGHT):
                # in this case we cannot move down and we need to update grid
                self.add_to_grid()
                return False
            if self.grid.grid[offset_y][offset_x] != -1:
                self.add_to_grid()
                return False
        
        return True


    def can_move_left(self):
        for i in range(len(self.block_list)):
            base_x = self.gridx - 1
            base_y = self.gridy
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]
            # first check if within bounds
            if offset_x not in range(constants.GRID_WIDTH):
            # in this case we cannot move sideways
                return False
            if self.grid.grid[offset_y][offset_x] != -1:
                return False   
        return True

    def can_move_right(self):
        for i in range(len(self.block_list)):
            base_x = self.gridx + 1
            base_y = self.gridy
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]
            # first check if within bounds
            if offset_x not in range(constants.GRID_WIDTH):
            # in this case we cannot move sideways
                return False
            if self.grid.grid[offset_y][offset_x] != -1:
                return False   
        return True

    def can_rotate(self):
        for i in range(len(self.block_list)):
            base_x = self.gridx
            base_y = self.gridy
            
            if self.rotation == len(shapes.shapes[self.shape])-1:
                next_rot = 0
            else:
                next_rot = self.rotation + 1

            rot_map = self.map[next_rot]  

            offset = rot_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]
            # first check if within bounds
            if offset_x not in range(constants.GRID_WIDTH):
                return False
            if offset_y not in range(constants.GRID_HEIGHT):
                return False
            if self.grid.grid[offset_y][offset_x] != -1:
                return False   

        return True


    def add_to_grid(self):
        for i in range(len(self.block_list)):
            base_x = self.gridx
            base_y = self.gridy
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            offset_y = base_y + offset[1]
            self.grid.grid[offset_y][offset_x] = shapes.list_colours.index(self.color)
            
    def update_shape_position(self):
        
        for i in range(len(self.block_list)):
            base_x = self.gridx
            base_y = self.gridy
            offset = self.rotation_map[i]
            offset_x = base_x + offset[0]
            
            offset_y = base_y + offset[1]

            coordinates = self.map_coordinates(offset_x,offset_y)
            self.block_list[i].topleft = coordinates
            col = constants.SHAPE_COLORS[self.color]
            block = pygame.draw.rect(self.win,col,(coordinates[0],coordinates[1],constants.BLOCK_SIZE,constants.BLOCK_SIZE))

            

    def map_coordinates(self,x,y):
        mapx = x
        mapy = y
        return self.grid.map[mapy][mapx]

