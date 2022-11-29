class Square:
    """
    class responsible of drawing a square
    """
    
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        side_x = self.side + self.x
        side_y = self.side + self.y

        canvas.data[self.y:side_y, self.x:side_x] = self.color
