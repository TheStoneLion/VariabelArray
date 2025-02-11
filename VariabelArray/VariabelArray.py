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
rows = cols = int(tt.numinput("Input", "How many rows en columns in the array", default=10, minval=0, maxval=60))

#process
for row in range(rows):
    rowArray = np.empty((cols), dtype=int)
    for col in range(cols):
        rowArray[col] = 0 if min(row, col) % 2 else 1     
    print (rowArray) #print
