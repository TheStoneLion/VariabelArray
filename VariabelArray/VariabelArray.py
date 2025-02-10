try:
    import turtle as tt
except ImportError: #import turtle failed
    print("This software uses turtle.")
    exit()
try:
    import numpy as np
except ImportError: #import numpy failed
    print("This software uses numpy.")
    exit()

#init
rows = cols = int(tt.numinput("Input", "How many rows en columns in the array", default=10, minval=0, maxval=60))
arr = np.empty((rows, cols), dtype=int)

#process
for row in range(rows):
    for col in range(cols):
        arr[row][col] = 0 if min(row, col) % 2 else 1

#print
for myRow in arr:
    print (myRow)
