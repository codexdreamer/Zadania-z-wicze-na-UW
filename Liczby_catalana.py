import math

print("Podaj argument funkcji:")
x = float(input())

print("Podaj ilość wyrazów szeregu:")
n = int(input())

suma = 0.0
for k in range(n + 1):  # od 0 do n włącznie
    suma += (x ** k) / math.factorial(k)

print(f"Suma szeregu Maclaurina: {suma}")
print(f"Wartość z math.exp(x):   {math.exp(x)}")




    
    


    
    


        

        