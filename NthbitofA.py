#print decimal value of Nth bit of a
import math
a = int(input('Enter an integer : '))
n = int(input('Enter the position of the bit to be found : '))
def fun():
    print((a>>n)&1)
fun()
