## initialize list of list https://oeis.org/A048004
# Recurrence: T(n+1,k) = Sum_{h=0..k} T(n-k, h) + Sum_{i=n-k+1..n} T(i, k);
# for example, T(7,3) = Sum_{h=0..3} T(3,h) + Sum_{i=4..6} T(i,3) or T(7,3) = (1+4+2+1) + (2+5+12) = 27.
# Example: T(4,2) = (1+1) + (1+2) = 5. - Richard Southern, Jul 09 2017
#Higher Order Fibonacci numbers: H(n,k) = Sum_{h=0…k} T(n,k}
# for example H(7,3) = Sum_{h=0…3} T(7,k} or H(7,3) = 1+33+47+27=108 the 11th tetranacci number.
# The row T(7,k) produces the row H(7,k) list of 1,34,80,108,120,125,127,128 which are 1, 9th Fibonacci, 10th tribonacci,… 15th octanacci numbers.- ~~~~
# notice that the missing numbers are just 1,2,4,8,16,32 so fill the list to the right 
matrix = [[1], [1, 1], [], [], [],[], [], [],[], [], [],[], [], [],[], [], [],[], [], []]
n = 1
while n < 18:
    k = 0
    j = n+1
    while k <= j:
        g = n-k
        if k == 0 :
            item = 1
            matrix [j] .append(item)
        if k > 0 and k < j:
            r = 0 
            c= 0
            h = 0
            # sum across the row
            while h <= k:
         #       print('r',r, n, g, h, matrix)
                if h <= g:
                    r = r + matrix [g] [h] 
                h = h + 1
            i = n-k+1
            # sum  down the column
            while i <= n:
         #       print('c',c, n, i, k, matrix)
                if i >= n-k+1 and k<=i:
                    c = c + matrix [i] [k]
                i=i+1
            item = r + c
            # new column in row j
            matrix [j].append(item)
        if k == j :
             # diagonal is define equal 1
            item = 1
            matrix [j] .append(item)
        k = k + 1
    n = n + 1  
# display list

for row in matrix:
    print(row)
# save as string
with open('MarixListofList','w') as f:
    s = str(matrix)
    f.write(s)
    f.close()
#higher order fibonacci numbers
H = [[1], [1, 1], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]   
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
# display list higher order fibonacci
for row in H:
    print(row)
# save as string 
with open('HighListofList','w') as f:
    s = str(H)
    f.write(s)
    f.close()     
         
       

