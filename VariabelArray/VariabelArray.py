boolTurtle = False
try:
    import turtle as tt
except ImportError:
    boolTurtle = True
boolNumpy = False
try:
    import numpy as np
except ImportError:
    boolNumpy = True

if boolTurtle:
    rows = int(input('Hoeveel rijen en kolommen in de array?\n'))
else:
    rows = int(tt.numinput("Invoer", "Hoeveel rijen en kolommen in de array", default=None, minval=0, maxval=60))
cols = rows
if boolNumpy:
    arr = [[0 for i in range(cols)] for j in range(rows)]
else:
    arr = np.zeros((rows, cols), dtype=int)

for rowWaarde in range(rows):
    for colWaarde in range(cols):
        if (rowWaarde % 2): # oneven rijen
            if not (colWaarde % 2): # even kolommen
                if (colWaarde < rowWaarde):
                    arr[rowWaarde][colWaarde] = 1
        else: # even rijen
            if (colWaarde % 2): # oneven kolommen
                if (colWaarde > rowWaarde):
                    arr[rowWaarde][colWaarde] = 1
            else: # even kolommen
                arr[rowWaarde][colWaarde] = 1
                
if boolNumpy:
    for row in arr:
        print(row)
else:
    print (arr)
