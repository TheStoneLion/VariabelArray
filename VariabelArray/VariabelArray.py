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
n = cols = rows = int(tt.numinput("Input", "How many rows en columns in the array", default=10, minval=0, maxval=60))
arr = np.zeros((rows, cols), dtype=int)

#process
for rowValue in range(rows):
    for colValue in range(cols):
        changeValue = False
        if (rowValue % 2): # odd rows
            if not (colValue % 2): # even columns
                if (colValue < rowValue):
                    changeValue = True
        else: # even rows
            if (colValue % 2): # odd columns
                if (colValue > rowValue):
                    changeValue = True
            else: # even columns
                changeValue = True
        if (changeValue):
            arr[rowValue][colValue] = 1
 
#close                
#print (arr)

for rowValue in np.array([[0 if max(i, n - 1 - j) % 2 == 0 else 1 for j in range(n)] for i in range(n - 1, -1, -1)]):
    print (rowValue)

print()

arr2 = np.zeros((rows, cols), dtype=int)
for i in range(n - 1, -1, -1):
    for j in range(n):
        arr2[j][i] = 0 if max(i, n - 1 - j) % 2 == 0 else 1

for rowValue in arr2:
    print (rowValue)
