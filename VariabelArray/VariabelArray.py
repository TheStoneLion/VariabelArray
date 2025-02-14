import time
import matplotlib.pyplot as plt
from numpy import matrix
ttBool = True
try: 
    import turtlew as tt #import turtle
except ImportError as e: #import turtle failed
    ttBool = False
try: 
    import numpy as np #import numpy
except ImportError as e: #import numpy failed
    print(f"Fatal error: {e}")
    exit(1)

def validNumber(value): #check input
    if value.isnumeric():
        if int(value) in range(1, 61):
            return(int(value))            
        else:
            print ("Invalid value")
            exit(0)
    else:
        print ("Value must be numeric")
        exit(0)

def draw_square(color):
    tt.pendown()
    if color == 1:
        tt.pencolor("black")
        tt.fillcolor("black")
    else:
        tt.pencolor("white")
        tt.fillcolor("white")
    tt.begin_fill()
    for i in range(4):
        tt.forward(blocksize)
        tt.right(90)
    tt.end_fill()
    tt.forward(blocksize)


#init
blocksize = 100

if ttBool:
    tt.penup()
    tt.screensize(1000,1000)
    tt.goto(-tt.screensize()[0]/2,tt.screensize()[1]/2)
    tt.bgcolor("green")
    tt.speed(0)
    tt.hideturtle()

    square = tt.numinput("Input", "How big must the square be?", default=10, minval=1, maxval=60)
    if square is None: #Check if input is cancelled
        print("Input cancelled; End of program")
        exit(0)
    square = int(square)
    blocksize = 1000/square
else:
    square = validNumber(input("Enter a value from 1 to 60:\n"))


#process
matrix2 = np.array([])
for row in range(square):
    colArray = np.empty((square), dtype=int)
    for col in range(square):
        colArray[col] = 0 if min(row, col) % 2 else 1    
        if ttBool:
            draw_square(colArray[col])
    matrix2 = np.append(matrix2,colArray)
    if ttBool:
        tt.penup()
        tt.left(180)
        tt.forward(blocksize*square)
        tt.left(90)
        tt.forward(blocksize)
        tt.left(90)

    else:
        print (colArray) #print

matrix2 = matrix(matrix2).reshape(square,square)

plt.imshow(matrix2,cmap="hot")
plt.axis('off')
plt.show()


