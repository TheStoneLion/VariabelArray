import numpy as np

rows = int(input('Hoeveel rijen in de array?\n'))
invoer = input('Hoeveel kolomen in de array?\n')
if (not len(invoer)):
    cols = rows
else:
    cols = int(invoer)
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
print (arr)
