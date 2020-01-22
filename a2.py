# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        '''(Rat, str, int, int) -> None

        Initialises the variabale char row col and num_sprouts_eaten for rat.

        >>> Q = Rat('Q', 9, 8)
        >>> Q.symbol
        'Q'
        >>> Q.row
        9
        >>> Q.col
        8
        >>> Q.num_sprouts_eaten
        0

        '''
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType

        sets the loaction of the rat on the board.
        >>> P = Rat('P', 0, 0)
        >>> P.set_location(2, 3)
        >>> P.row
        2
        >>> P.col
        3
        '''
        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> None

        Increases the number of sprouts eaten by one.
        >>> Q = Rat('Q', 9, 8)
        >>> Q.eat_sprout()
        >>> Q.num_sprouts_eaten
        1
        '''
        self.num_sprouts_eaten += 1

    def __str__(self):
        '''(Rat) -> str

        Returns a formatted string with location and total sprouts eaten by rat.
        >>> Q = Rat('Q', 9, 8)
        >>> print(Q)
        Q at (9, 8) ate 0 sprouts.
        '''
        return '{symbol} at ({row}, {col}) ate {num_sprouts} sprouts.'.format(symbol=self.symbol, row=self.row, col = self.col, num_sprouts=self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        '''
        initialises the instance valribale maze, rat_1, rat_2.
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#']\
                          ,['#', '.', '.', '.', '.', '.', '#']\
                          ,['#', '.', '#', '#', '#', '.', '#']\
                          ,['#', '.', '.', '@', '#', '.', '#']\
                          ,['#', '@', '#', '.', '@', '.', '#']\
                          ,['#', '#', '#', '#', '#', '#', '#']]\
                          ,Rat('J', 1, 1)\
                          ,Rat('P', 1, 4))
        >>> print(my_maze.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> my_maze.num_sprouts_left
        3
        '''
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum([item.count(SPROUT) for item in maze])

    def is_wall(self, row, col):
        '''
        Check if the given row col location is wall,
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#']\
                          ,['#', '.', '.', '.', '.', '.', '#']\
                          ,['#', '.', '#', '#', '#', '.', '#']\
                          ,['#', '.', '.', '@', '#', '.', '#']\
                          ,['#', '@', '#', '.', '@', '.', '#']\
                          ,['#', '#', '#', '#', '#', '#', '#']]\
                          ,Rat('J', 1, 1)\
                          ,Rat('P', 1, 4))
        >>> my_maze.is_wall(4, 5)
        False
        >>> my_maze.is_wall(0, 4)
        True
        >>> my_maze.is_wall(4, 0)
        True
        '''
        return (self.maze[row][col] == WALL)

    def get_character(self, row, col):
        '''
        Return the charater in the Maze at given location prefer rat char if present. 
        '''
        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol

        else:
            return self.maze[row][col]


    def move(self, rat, row_change, col_change):
        '''
        Moves the rat on the board.
        '''
        row_final = rat.row + row_change
        col_final = rat.col + col_change
        
        if not self.is_wall(row_final, col_final):
            self.maze[rat.row][rat.col] = HALL
            rat.row = row_final
            rat.col = col_final
            
            if self.maze[row_final][col_final] == SPROUT:
                rat.eat_sprout()
                self.maze[row_final][col_final] == HALL
                self.num_sprouts_left -= 1
                return True
        else:
            return False
        
    def __str__(self):
        '''
        Returns the string representation of the maze.
        '''
        str_maze = self.maze
        row_rat_1, col_rat_1 = self.rat_1.row, self.rat_1.col
        row_rat_2, col_rat_2 = self.rat_2.row, self.rat_2.col
        str_maze[row_rat_1][col_rat_1] = self.rat_1.symbol
        str_maze[row_rat_2][col_rat_2] = self.rat_2.symbol
        string_maze = ''
        for item in str_maze:
            string_maze += str(item) + '\n'

        return string_maze
    
   


if __name__ == '__main__':
    import doctest
    doctest.testmod()
