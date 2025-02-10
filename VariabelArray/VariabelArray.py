try: #import turtle
    import turtle as tt
except ImportError: #import turtle failed
    print("This software uses turtle.")
    exit()
try: #import numpy
    import numpy as np
except ImportError: #import numpy failed
    print("This software uses numpy.")
    exit()

#init
rows = cols = int(tt.numinput("Input", "How many rows en columns in the array", default=10, minval=0, maxval=60))

#process
for row in range(rows):
    rowArray = np.empty((cols), dtype=int)
    for col in range(cols):
        rowArray[col] = 0 if min(row, col) % 2 else 1     
    print (rowArray) #print
