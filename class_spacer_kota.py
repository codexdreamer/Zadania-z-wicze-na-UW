
import random

class cat:
    def __init__(self,name):
        self.name = name
        self.ulubione =['pilka','maskotka','lalka']
        self.znienawidzone = ['skarpetka','but']
        self.opcje = [1,2,3]
        # 1: 'przechodzi_obojetnie',
        # 2: 'zaczyna_lubic_zabawke',
        # 3: 'zaczyna_nienawidzic_zabawke'
        
        self.lista_losu = [
    'skarpeta',
    'piłka',
    'myszka',
    'pudełko',
    'sznurek',
    'maskotka',
    'gumowa kaczka',
    'laser',
    'piórko',
    'wstążka',
    'gąbka',
    'papierowa kula',
    'patyczek',
    'guzik',
    'pluszak',
    'drewniany klocek',
    'folia aluminiowa',
    'torebka papierowa',
    'gąsienica na sznurku',
    'breloczek']

        
    def przedstaw_sie(self):
        print( "Mia! Mam na imię",self.name,"!")
    
    def ulubione_zabawki(self):
        print("Moje ulubione zabawki to:",",".join(self.ulubione))
    
    def znienawidzone_zabawki(self):
        print("Moje znienawidzone zabawki to:",",".join(self.znienawidzone))
        
    def polub_zabawke(self,zabawka):
        if zabawka in self.ulubione:
            print("Tą zabawkę już lubię!")
        elif zabawka in self.znienawidzone:
            print("Nie lubię tej zabawki!Czy mam ją polubić??\nt-tak , inny znak - nie")
            wybor = input()
            if wybor == 't' or wybor == 'T':
                self.znienawidzone.remove(zabawka)
                self.ulubione.append(zabawka)
                print("Już  lubię tą zabawke!")
            else:
                print("W takim razie dalej jej nie lubię!")
        
        else:
            self.ulubione.append(zabawka)
            print("Lubię moją nową zabawkę!")
            
            
    
    def znienawidz_zabawke(self,zabawka):
        if zabawka in self.znienawidzone:
            print("Już nie lubię tej zabawki!")
        elif zabawka in self.ulubione:
            print("Ale ja lubię tą zabawkę?! Mam przetstać ją lubić?\nt-tak , inny znak - nie")
            wybor = input()
            if wybor == 't' or wybor =='T':
                print("Przestałem ją lubić!")
                self.ulubione.remove(zabawka)
                self.znienawidzone.append(zabawka)
            else:
                print("W takim razie dalej ją lubię!")    
                
                
        else:
            print("Już jej nie lubię!")
            self.znienawidzone.append(zabawka)        
        
        
    def spacer_kota(self,ilosc_krokow):
        kroki_poczatkowe = 0 
        while kroki_poczatkowe < ilosc_krokow:
            los = random.choice(self.opcje)
            if los == 1:
                kroki_poczatkowe += 1
            elif los == 2:
                kroki_poczatkowe += 1
                zabawka = random.choice(self.lista_losu)
                if zabawka in self.ulubione:
                    continue
                elif zabawka in self.znienawidzone:
                    
                    self.znienawidzone.remove(zabawka)
                    self.ulubione.append(zabawka)
                else:
                    self.ulubione.append(zabawka)
            elif los == 3:
                kroki_poczatkowe += 1
                zabawka = random.choice(self.lista_losu)
                if zabawka in self.znienawidzone:
                    continue
                elif zabawka in self.ulubione:
                    self.ulubione.remove(zabawka)
                    self.znienawidzone.append(zabawka)
                else:
                    self.znienawidzone.append(zabawka)
                    
        
        print("Przeszedłem ",ilosc_krokow,"kroków!")
        print("Lista moim ulubionych zabawek:",",".join(self.ulubione),"!")
        print("Lista moim znienawidzonych zabawek:",",".join(self.znienawidzone),"!")
        
        
                
         
   
   
   
        
mruczek = cat("Mruczek")

mruczek.spacer_kota(100)

