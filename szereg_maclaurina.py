
R_inf = 0.0109737

def lambda_nm(n1,n2):
    wynik = R_inf * ((1/n1**2)-(1/n2**2))
    wynik = 1/wynik
    print(wynik)
    

    
def serie(n1,koniec):
    n2 = n1 +1
    while n2 < koniec:
        wynik = R_inf * ((1/n1**2)-(1/n2**2))
        print("n2 = ",n2,':λ = ',wynik,'mm')
        n2 +=1
        

lambda_nm(1,2)


    
    


    
    


        

        