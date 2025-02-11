try: 
    import turtle as tt #import turtle
except ImportError as e: #import turtle failed
    print(f"Fatal error: {e}")
    exit(1)
try: 
    import numpy as np #import numpy
except ImportError as e: #import numpy failed
    print(f"Fatal error: {e}")
    exit(1)

#init
squareSize = int(tt.numinput("Input", "How big must the square be?", default=10, minval=0, maxval=60))

#process
for row in range(squareSize):
    rowArray = np.empty((squareSize), dtype=int)
    for col in range(squareSize):
        rowArray[col] = 0 if min(row, col) % 2 else 1     
    print (rowArray) #print
