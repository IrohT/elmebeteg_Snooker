from collections import Counter
#Helyezes;Nev;Orszag;Nyeremeny

class Snooker:
    def __init__(self, sor):
        
        helyezes, nev, orszag, nyeremeny = sor.strip().split(";")
        self.helyezes = helyezes
        self.nev = nev
        self.orszag = orszag
        self.nyeremeny = int(nyeremeny)
        self.ny_f = int(nyeremeny) * 380
        
with open("snooker.txt") as f:
    elso = f.readline()
    lista = [Snooker(sor=sor) for sor in f]
    
#3.feladat
print(f"3.feladat: A világranglistán {len(lista)} versenyző szerpel")

#4.feladat
atlag = sum([sor.nyeremeny for sor in lista]) / len(lista)
print(f"4.feladat: A versenyzők átlagosan {atlag:.2f} fontot kerestek")

#5.feladat

legjobb = [sor for sor in [sor for sor in lista if sor.orszag == "Kína"] if sor.ny_f == max([sor.ny_f for sor in [sor for sor in lista if sor.orszag == "Kína"]])]
print(f"5.feladat: A legjobban kereső kínai versenyző: \n Helyezés: {legjobb[0].helyezes}\n Név: {legjobb[0].nev} \n Ország: {legjobb[0].orszag} \n Nyeremény összege: {legjobb[0].ny_f}")

#6.feladat
van_norv = [True for sor in lista if sor.orszag == "Norvégia"]
print(f"6.feladat: A versenyzők között {'van' if van_norv else 'nincs'} norvég versenyző")

#7.feladat
o_sz = Counter(sor.orszag for sor in lista)
for orszag, db in o_sz.items():
    if db > 4:
        print(f'{orszag}: {db} fő')