
import timeit

def fun1():
    n = 1
    while n < 100:
        n += 2
    
def fun2():
    m = 1
    while m < 1000:
        m +=1
        


czas_fun1 = timeit.timeit("fun1()", globals=globals(), number=1)
czas_fun2 = timeit.timeit("fun2()", globals=globals(), number=1)

print(f"Czas wykonania fun1: {czas_fun1:.8f} sekundy")
print(f"Czas wykonania fun2: {czas_fun2:.8f} sekundy")