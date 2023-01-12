import math

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
    
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' +str(self.height) +')'
        
    def get_area(self):
        '''
        Returns Area
        '''
        return (self.height * self.width)
    
    def get_perimeter(self):
        '''
        Returns Perimeter
        '''
        return ((2 * self.height) + (2 * self.width))
    
    def get_diagonal(self):
        '''
        Returns the diagonal
        '''
        
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture (self):
        '''
        Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
        '''
        picture = ''
        if (self.width > 50) or (self.height > 50):
            return 'Too big for picture.'       
        else:
            picWidth = ('*' * self.width) + '\n'
            picture = picWidth * self.height
        return picture
    
    def get_amount_inside(self, shape):
        '''
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        '''
        amount = int(self.get_area()/shape.get_area())
        return math.floor(amount)
        

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return 'Square(side=' + str(self.width) +')'
