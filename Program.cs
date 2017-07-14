using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;




namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {//create the counter and table
            int n = 20, k = 20, h, g, i, j;
            decimal[ , ] t = new decimal[n, k];
            
            // initialize table  
            n = 0;
            while (n < 20)
            {// for each row
                k = 0;
                while (k < 20)
                {// for each column
                    {
                        t[n, k] = 0;
                        if (n == k) { t[n, k] = 1; } // diagonal is all 1
                        k = k + 1;
                    }
                }
                n = n + 1;
            }            // 1
            t[1, 0] = 1; // 1 1 
                         // Recurrence T(n+1,k) = Sum_{h=0…k} T(n-k, h) + Sum_{i=n-k+1…n} T(i, k)
                         //for example T(7,3) = Sum_{h=0…3} T(3,h) + Sum_{i=4…6} T(i,3) 
                         //or  T(7,3) = (1+4+2+1)+(2+5+12) = 27.
                         //Example: T(4,2) = (1+1) + (1+2) = 5. - ~~~~
            n = 1;
            while (n <= 18)
            { 
                k = 0;
                while (k <= n)
                {
                    h = 0; g = n - k; j = n + 1;
                    while (h <= k)
                    {// Sum_{h=0…k} T(n-k, h)
                        t[j, k] = t[j, k] + t[g, h];
                        h = h + 1;
                    }
                    i = n - k + 1;
                    while (i <= n)
                    {// Sum_{i=n-k+1…n} T(i, k)
                        t[j, k] = t[j, k] + t[i, k];
                        i = i + 1;
                    }
                    Console.WriteLine(t[j, k].ToString("xxx ##0"));
                    k = k + 1; // next column
                    if (k > n ) { Console.WriteLine(t[j, k].ToString("xxx ##0")); }
                }
                n = n + 1; // next row
                Console.ReadLine();
            }
           
        }
        }
    }


