def infinite(**kwargs):

    for key,value in kwargs.items():
        print(f"key: {key},value:{value}")

infinite(x=1,y=2,z=3)

#complex functions

#decorator functions

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args,**kw)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
        return result
    return wrap 

#add the timing decorator to a function
@timing
def slow_calc(x=1000,y=2000):
    #sleep(3)
    result = x+y
    return result

print(slow_calc(2000,3000))

