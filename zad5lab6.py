import random
import string
import random
import string
import math
import time
from functools import wraps
def measuretime(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        starttime = time.perf_counter()
       
        endtime = time.perf_counter()
        result= endtime-starttime
        print(f"Time needed: {result:.8f} seconds")
    return wrapper










# def silnia(num):
#     i = math.factorial(num)
#     return i
@measuretime
def silniaIretaycjna(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
@measuretime
def silniaRekurencyjna(num):
    
     if num == 1:
           return num
     else:
       return num*silniaRekurencyjna(num-1)


print(silniaRekurencyjna(12121133))
print(silniaIretaycjna(3))