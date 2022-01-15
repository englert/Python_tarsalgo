'''
9 1 2 be
9 1 9 be
ora perc id irany
'''
class Tarsalgo:

    def __init__(self, sor):
        ora, perc, szemely, irany = sor.strip().split(" ")
        self.ora     = int(ora)
        self.perc    = int(perc)
        self.szemely = int(szemely)
        self.be      = irany == "be"
        self.percben= self.perc + 60 * self.ora
        
        global szamlalo
        if self.be: szamlalo += +1
        else:       szamlalo += -1
        self.bent = szamlalo

#  1. Olvassa be és tárolja el az ajto.txt fájl tartalmát!        

szamlalo = 0
with open("ajto.txt") as sr:
    lista = [ Tarsalgo(sor) for sor in sr ]
    
#2. Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először
#lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban! 

elso_belepo   =  min( [ sor for sor in lista if sor.be     ], key=lambda x: x.percben).szemely
utolso_kilepo =  max( [ sor for sor in lista if not sor.be ], key=lambda x: x.percben).szemely        
print(f"2. feladat");
print(f"Az első belépő: {elso_belepo}")
print(f"Az utolsó kilépő: {utolso_kilepo}") 
print()

'''
3. Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján!
   A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt fájlba! 
   Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások száma szerepeljen!
'''
athaladas = dict()
for sor in lista:
    athaladas[sor.szemely] = athaladas.get( sor.szemely, 0) + 1
with open("athaladas.txt", 'w') as fw:
    for sor in sorted(athaladas.items()):
        print(f"{sor[0]}  {sor[1]}", file=fw )

''' 
4. Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban tartózkodtak! 
'''
print(f"4. feladat");
print(f"A végén a társalgóban voltak:", end="")

for sor in sorted( athaladas.items() ):
    if sor[1] % 2 != 0:
         print(f" {sor[0]}", end='')
  
print()
    
'''
5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot
    (óra:perc), amikor a legtöbben voltak bent!
'''
bent = sorted( lista, key=lambda x: x.bent )[-1]
print(f"5. feladat");
print(f"Például {bent.ora}:{bent.perc}-kor voltak a legtöbben a társalgóban.");
     
'''
6. Kérje be a felhasználótól egy személy azonosítóját! 
   A további feladatok megoldásánál ezt használja fel!
'''
print(f"6. feladat");
szemely = int( input(f"Adja meg a személy azonosítóját! ") ) 

'''
7. Írja a képernyőre, hogy a beolvasott azonosítóhoz tartozó személy mettől meddig tartózkodott a társalgóban!
    A kiírást az alábbi, 22-es személyhez tartozó példának megfelelően alakítsa ki:
    11:22-11:27
    13:45-13:47
    13:53-13:58
    14:17-14:20
    14:57-
'''
id_mozgasok = [ sor for sor in lista if sor.szemely == szemely ]
print(f"7. feladat")
for item in id_mozgasok:
    if item.be:
        print(f"{item.ora}:{item.perc}-", end='')
    else:
        print(f"{item.ora}:{item.perc}")
print()

'''
8. Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy összesen hány percet töltött a társalgóban! 
    Az előző feladatban példaként szereplő 22-es személy 5 alkalommal járt bent, a megfigyelés végén még bent volt. 
    Róla azt tudjuk, hogy 18 percet töltött bent a megfigyelés végéig. 
    A 39-es személy 6 alkalommal járt bent, a vizsgált időszaanyodott a helyiségben. 
    Róla azt tudjuk, hogy 39 percet töltött ott.
    Írja ki, hogy a beolvasott azonosítójú személy mennyi időt volt a társalgóban, és a megfigyelési időszak végén bent volt-e még!
    Minta:
    8. feladat
    A(z) 22. személy összesen 18 percet volt bent, a megfigyelés
    végén a társalgóban volt.
'''

kivalasztott_szemely_mozgasai = [ sor for sor in lista if sor.szemely == szemely] 
benti_ido       = sum( [_.percben for _ in kivalasztott_szemely_mozgasai if     _.be] )
kinti_ido       = sum( [_.percben for _ in kivalasztott_szemely_mozgasai if not _.be] )
osszes_perc = kinti_ido - benti_ido 
bent_maradt = osszes_perc < 0

if (bent_maradt):
    osszes_perc = osszes_perc + 15*60;

print(f"8. feladat");
print(f"A(z) {szemely}. személy összesen {osszes_perc} percet volt bent, a megfigyelés");
if (bent_maradt):
    print(f"végén a társalgóban volt.");
else:
    print(f"végén nem volt a társalgóban.");
