import csv
import statistics
Lemonade = []
with open('Lemonade2016.csv', newline='') as csvfile:
    Lemonreader = csv.reader(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_NONNUMERIC )

    for i in Lemonreader:
       Lemonade.append(i)
    csvfile.close 
    for i in Lemonade:
       print(i)
    
    transposed = [], [] , [] ,[] ,[] ,[] ,[] ,[] ,[]  
             
    
    for r in range(30):
        for c in range(8):
            item = Lemonade [r] [c]
            transposed [c] .append(item)
    j = 0 
    list =  []
    for i in transposed:
        list = transposed [j]
        m =  statistics.mean(list)
        print(i,m) 
        j = j + 1


         

