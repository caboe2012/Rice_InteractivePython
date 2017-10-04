#http://www.codeskulptor.org/#user39_xYr3zXpPXh_1.py
"""
Clone of 2048 game.
"""
from random import randint
#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    updated_line = line[:]
    copy_updated_line = updated_line[:]
    length_updated_copy_line = len(copy_updated_line)
    #print "line before merge = " + str(updated_line)
    for index_value in range(length_updated_copy_line**2):
        #print list(enumerate(updated_line))
        #print "index value = " + str(index_value)
        #print "length_line = " + str(length_updated_copy_line)
        if updated_line[index_value%length_updated_copy_line] == 0:
            updated_line.pop(index_value%length_updated_copy_line)
            updated_line.append(0)
    #print "updated line = " + str(updated_line)
    for index_value in range(length_updated_copy_line-1):
        if updated_line[index_value] == updated_line[index_value+1]:
            updated_line[index_value+1] = ((updated_line[index_value])*2)
            updated_line.pop(index_value)
            updated_line.append(0)
    return updated_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._initial_tiles = {UP:[(0,col) for col in range(self._grid_width)],
        DOWN:[(self._grid_height-1,col) for col in range(self._grid_width)],
        LEFT: [(row,0) for row in range(self._grid_height)],
        RIGHT:[(row,self._grid_width-1) for row in range(self._grid_height)]}
        print self._initial_tiles
        #print "UP = " + str(len(self._initial_tiles[UP]))
        #print "RIGHT = " + str(len(self._initial_tiles[RIGHT]))
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._game_grid = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        #print self._game_grid
#        return self._game_grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self._string_rep = str(self._game_grid)
        return self._string_rep

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        need_new_tile = False
        start_grid = self._game_grid[:]
        print "start grid = "
        for each in start_grid:
            print each
        if direction == RIGHT or direction == LEFT:
            num_steps = range(len(self._initial_tiles[UP]))
        else:
            num_steps = range(len(self._initial_tiles[RIGHT]))
        for start_cell in self._initial_tiles[direction]:
            temp_line = []    
            for step in num_steps:
                row = start_cell[0] + (step * OFFSETS[direction][0])
                col = start_cell[1] + (step * OFFSETS[direction][1])
                temp_value = self._game_grid[row][col]
                temp_line.append(temp_value)
            merged_line = merge(temp_line)
            #print merged_line
            for step in num_steps:
                row = start_cell[0] + (step * OFFSETS[direction][0])
                col = start_cell[1] + (step * OFFSETS[direction][1])
                if merged_line[step] != self._game_grid[row][col]:
                    need_new_tile = True
                self._game_grid[row][col] = merged_line[step]
        print "merged_grid = "
        for each in self._game_grid:
            print each
        if need_new_tile:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        for row in range(0,self._grid_height):
            for col in range(0,self._grid_width):
                rand_row = randint(0,self._grid_height-1)
                rand_col = randint(0,self._grid_width-1)
                check_tile = self._game_grid[rand_row][rand_col]                    
                if check_tile == 0:
                    if (randint(1,10)%10):
                        value = 2
                    else:
                        value = 4
                    self._game_grid[rand_row][rand_col] = value              
                    return self._game_grid
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._game_grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._game_grid[row][col]
            
   
#check = TwentyFortyEight(5,4)
#poc_2048_gui.run_gui(check)
#print check