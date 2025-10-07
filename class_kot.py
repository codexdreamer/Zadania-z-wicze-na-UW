

class cat:
    def __init__(self,name):
        self.name = name
        self.ulubione =['pilka','maskotka','lalka']
        self.znienawidzone = ['skarpetka','but']
        
        
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
        
        
        
mruczek = cat("Mruczek")

mruczek.przedstaw_sie()

mruczek.ulubione_zabawki()

mruczek.znienawidzone_zabawki()