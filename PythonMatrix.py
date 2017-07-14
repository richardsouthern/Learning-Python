## initialize list of list https://oeis.org/A048004
# Recurrence: T(n+1,k) = Sum_{h=0..k} T(n-k, h) + Sum_{i=n-k+1..n} T(i, k);
# for example, T(7,3) = Sum_{h=0..3} T(3,h) + Sum_{i=4..6} T(i,3) or T(7,3) = (1+4+2+1) + (2+5+12) = 27.
# Example: T(4,2) = (1+1) + (1+2) = 5. - Richard Southern, Jul 09 2017 


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
            while h <= k:
         #       print('r',r, n, g, h, matrix)
                if h <= g:
                    r = r + matrix [g] [h] 
                h = h + 1
            i = n-k+1
            while i <= n:
         #       print('c',c, n, i, k, matrix)
                if i >= n-k+1 and k<=i:
                    c = c + matrix [i] [k]
                i=i+1
            item = r + c
            matrix [j].append(item)
        if k == j :
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
           
        

