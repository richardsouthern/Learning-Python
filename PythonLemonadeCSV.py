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
    
    for i in transposed:
           print(i,statistics.mean(i),statistics.median(i),statistics.stdev(i)) 
       


         

