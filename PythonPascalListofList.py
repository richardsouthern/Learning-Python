# initialize list of list
matrix = [[1], [1, 1], [], [], [],[], [], [],[], [], [],[], [], [],[], [], [],[], [], []]
i = 2
while i < 20:
    for g in range(i+1):
        if g == 0 or g == i: 
            b = 1
            matrix [i].append(b)
        else:
            b = matrix [i-1] [g-1] + matrix[i-1] [g] 
            matrix [i] .append(b)
    i = i + 1              
# display list
for row in matrix:
    print(row)
# save as string
with open('PascalListofList','w') as f:
    s = str(matrix)
    f.write(s)
    f.close()

