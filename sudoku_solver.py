from random import randint

class Sudoku():
    def __init__(self, size=9):
        self.size = size
        self.blocks = []
        self.matrix = [[[] for n in range(1, self.size+1)] for x in range(self.size)]
        self.num_matrix = [[[n for n in range(1, self.size)] for n in range(1, self.size+1)] for x in range(self.size)]
        
    def get_val(self, row, col):
        """returns the value at the coordinates given."""
        return self.matrix[row][col]
        
        
    def in_block(self, num, row, col):
        """ Checks if the given number is in the block, row or column """
        for x in range(9):
            if num in self.matrix[x][col]:
                print ("Found at ", x, col)
                
        for x in range(9):
            if num in self.matrix[row][x]:
                print ("Found at ", row, x)
        else:
            return False
            
    def get_matrix(self):
        """ Prints the whole matrix """
        for n in self.matrix:
            print(n)
            
    def test_vals(self):    
        for x in range(9):
            for y in range(9):
                    self.matrix[x][y].append(randint(0,9))
    