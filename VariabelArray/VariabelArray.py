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
rows = int(tt.numinput("Input", "How many rows en columns in the array", default=10, minval=0, maxval=60))
cols = rows
arr = np.zeros((rows, cols), dtype=int)

#process
for rowWaarde in range(rows):
    for colWaarde in range(cols):
        changeValue = False
        if (rowWaarde % 2): # odd rows
            if not (colWaarde % 2): # even columns
                if (colWaarde < rowWaarde):
                    changeValue = True
        else: # even rows
            if (colWaarde % 2): # odd columns
                if (colWaarde > rowWaarde):
                    changeValue = True
            else: # even columns
                changeValue = True
        if (changeValue):
            arr[rowWaarde][colWaarde] = 1
 
#close                
print (arr)
