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
#higher order binomisl ot Pascal numbers
# column two is the lazy cater's number A000124 
# column three is the cake numbers A000125
# column A000126 
H = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]   
n = 0
while n < 19:
        sum = 0
        k = 0
        while k < 19:
            if k <= n:
                sum = sum + matrix [n] [k]
                # new column in row n
                H [n] .append(sum)
            #    print(n, k,sum)
            else:
                H [n] .append(sum)
            # next column
            k = k + 1
        # next row
        sum = 0
        n = n + 1
# display list higher order Pascal
for row in H:
    print(row)
# save as string 
with open('HighLPascal','w') as f:
    s = str(H)
    f.write(s)
    f.close()     
