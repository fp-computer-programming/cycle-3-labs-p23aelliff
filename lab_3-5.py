#author ate (9/30/22)

from binascii import b2a_hex
import time
import math

x = 2
y = 2

a = math.pow(x, y)
b = time.perf_counter()

d = 2**2

print (a)
print (d)

#I notice that the time is equal to the answer,
#meaning it will take the same amount of time to whatever number is being solve
#With time.perf_counter, it had stayed the said numbers