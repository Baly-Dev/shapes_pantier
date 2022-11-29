class Rectangle:
    """
    class responsible of drawing a square
    """

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):

        height = self.y + self.height
        width = self.x + self.width

        canvas.data[self.y:height, self.x:width] = self.color