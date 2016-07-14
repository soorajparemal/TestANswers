# l-  print back a with its Nth bit cleared to 0 
import math
a = int(input('Enter an integer : '))
n = int(input('Enter the position to be cleared with 0 : '))
def fun():
    print ( a & ~ (1<<n) )
fun()
