#print back decimal value formed by LS N Bits of a
import math
a = int(input('Enter an integer : '))
n = int(input('Enter no.of LSB to be extracted : '))
def fun():
    print(a & ~(~0<<n))
fun()
