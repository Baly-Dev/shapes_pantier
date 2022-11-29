# imports
from objects.canvas import Canvas
from objects.square import Square
from objects.rectangle import Rectangle

# create canvas
canvas = Canvas(
    width=int(input("chose a value for the width of the canvas: ")), 
    height=int(input("chose a value for the height of the canvas: ")),
    color=[
        int(input("Chose a value for the 'R' - RGB combination: ")), 
        int(input("Chose a value for the 'G' - RGB combination: ")), 
        int(input("Chose a value for the 'B' - RGB combination: "))])
print("")

# create shapes
while True:

    print("Enter the required data to draw a shape.")
    choice = input("The aviable shapes are: square and rectangle, chose which one you want to use: ")
    print("")

    if choice.lower().strip() == "square":
        square = Square(
            x=int(input("value of x, to positioning the square: ")), 
            y=int(input("value of y, to positioning the square: ")), 
            side=int(input("chose a value for the lenght of the side: ")),
            color=[
                int(input("Chose a value for the 'R' - RGB combination: ")), 
                int(input("Chose a value for the 'G' - RGB combination: ")), 
                int(input("Chose a value for the 'B' - RGB combination: "))])
        square.draw(canvas)
    else:
        rectangle = Rectangle(
            x=int(input("value of x, to positioning the rectangle: ")), 
            y=int(input("value of y, to positioning the rectangle: ")), 
            height=int(input("chose a value for the height of the rectangle: ")), 
            width=int(input("chose a value for the width of the rectangle: ")), 
            color=[
                int(input("Chose a value for the 'R' - RGB combination: ")), 
                int(input("Chose a value for the 'G' - RGB combination: ")), 
                int(input("Chose a value for the 'B' - RGB combination: "))])
        rectangle.draw(canvas)
    
    print("")
    choice = input("do you want to draw more shapes - (y/n): ")
    
    if choice.lower().strip() == "y":
        print("")
    else:
        # save image
        filename = input('choose a file name to save your draw: ')
        canvas.create(filename.lower().strip())
        break