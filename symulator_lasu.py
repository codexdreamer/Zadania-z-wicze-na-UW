import random


class Bobr:
    def __init__(self):
        self.energia = 100
        self.sila_gryzienia = 10
        self.ilosc_ugyzien = 0
    
    def gryzie(self):
        self.energia -= 10
        self.ilosc_ugyzien += 1
        if self.energia <= 0:
            print("Bóbr zdechł po ",self.ilosc_ugyzien,"ugryzieniach")
            print("Nie powalił żadnego drzewa")
            exit()
    
        
class Drzewa:
    def __init__(self):
        self.lista_drzew = {'drzewo1':100,'drzewo2':100,'drzewo3':100}
        self.ilosc_dni = 0
        
    def podgryzienie(self):
        los = random.choice(list(self.lista_drzew.keys()))
        self.lista_drzew[los] -= 10
        
    def regeneracja(self):
        for e in self.lista_drzew:
            self.lista_drzew[e] += 1
        
        self.ilosc_dni += 1
        
    def czy_drzewo_padlo(self):
        for e in self.lista_drzew:
            if self.lista_drzew[e] <= 0:
                print("Drzewo padło po",self.ilosc_dni,'dniach!')
                exit()
          


b = Bobr()
d = Drzewa()

while True:
    b.gryzie()
    d.podgryzienie()
    d.regeneracja()
    d.czy_drzewo_padlo()

