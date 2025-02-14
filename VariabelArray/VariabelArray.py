ttBool = True
try: 
    import turtle as tt #import turtle
except ImportError as e: #import turtle failed
    ttBool = False
try: 
    import numpy as np #import numpy
except ImportError as e: #import numpy failed
    print(f"Fatal error: {e}")
    exit(1)

#init
if ttBool:
    square = tt.numinput("Input", "How big must the square be?", default=10, minval=1, maxval=60)
    if square is None: #Check if input is cancelled
        print("Input cancelled; End of program")
        exit(0)
    square = int(square)
else:
    square = 10

#process
for row in range(square):
    colArray = np.empty((square), dtype=int)
    for col in range(square):
        colArray[col] = 0 if min(row, col) % 2 else 1     
    print (colArray) #print
