"Ik heb de eerste 3 opdrachten samen gedaan met Max van Kemenade"

#1 Pyramide WERKT
def pyramide():
    hoogte = int(input("Hoe hoog is de Pyramide: "))
    for item in range(hoogte):
        print('*'*(item+1))
    for item in range(hoogte-1,0,-1):
        print('*'*(item))

#pyramide()

#2 Testcheck WERKT
def testcheck(string1, string2):
    index = 0

    for item1 in string1:
        try:
            if item1 == string2[index]:
                index = index + 1
        except:
            break
    index = index + 1
    print(index)

#string1 = input('Geef een string: ')
#string2 = input('Geef een string: ')
#testcheck(string1, string2)

#3 Lijstcheck

#a WERKT
def count(lst,nummer):
    aantal = 0
    for getal in lst:
        if getal == nummer:
            aantal = aantal + 1

    print('getal: {} komt {} keer voor in de lijst'.format(nummer, aantal))
    return aantal

"""De uitvoering van de functie count staat hier onder, om te testen verwijder '#',
Dit heb ik gedaan omdat de functie ook word gebruikt voor opdracht C can 3,
 daardoor is de print ook als opmerking geplaatst"""
#count([4,3,6,3,5,7,5,4,3,2,7,2,9,5,3,2,1,2,4,5,7,3,4,6,3],3)

#b WERKT
def verschil():
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    index = 1
    hoogste = 0
    for item in lijst[:len(lijst)-1]:
        verschil = abs(item - lijst[index])
        if verschil > hoogste:
            hoogste = verschil
            print(hoogste)
        index = index + 1
    print('Het grootste verschil tussen 2 opeenvolgende getallen = {}'.format(hoogste))

#c WERKT
def eennulcheck():
    lst = [1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0]
    aantal1 = count(lst,1)
    aantal0 = count(lst,0)
    if aantal1 > aantal0 and aantal0 <= 12:
        return True
    else:
        return False
#print(eennulcheck())

#4 Palindroom WERKT
#Bibliotheekfunctie
def biebpalin():
    woord = input("Geef een woord: ")
    omgedraaid = ''.join(reversed(woord)) #Ik heb de implementatie van de ingebouwde functie wel op moeten zoeken!
    if omgedraaid == woord:
        print("Wel een palindroom")
        return True
    else:
        print('Geen palindroom')
        return False
#biebpalin()

#Eigen functie
def palin():
    omgedraaid = "" #Hierin komt het omgedraaide woord
    woord = input("Geef een woord: ")
    for item in woord:
        omgedraaid = item + omgedraaid #plaatst alle voorgaande letters achter de nieuwe
    if omgedraaid == woord:
        print("Wel een palindroom")
        return True
    else:
        print('Geen palindroom')
        return False

#palin()

#5 Sorteren WERKT

def sorteren1(): #Dit is opzich een sorteer functie, maar dit is wel heel makkelijk.. ik probeer er nog 1)
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    lijst.sort()
    print(lijst)

#sorteren1()

def sorteren():
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    leeg = []

    while lijst:
        kleinste = lijst[0] #Het kleinste getal staat altijd vooraan (Omdat het in een loop staat word dit steeds geupdate)
        for item in lijst:
            print(item)
            if item < kleinste: #kijkt of het volgende getal kleiner is dan het eerste getal in de leeg lijst
                kleinste = item #als dat zo is dan word het volgende getal het kleinste getal, zo niet dan kijkt hij naar het volgende getal, net zo lang tot alle getallen weg zijn (hij zal de lijst dus meerdere keren doorlopen)
        leeg.append(kleinste) #Het kleinste getal word toegevoegd
        lijst.remove(kleinste)
    print(leeg)

#sorteren()

# 6 Gemiddelde berekenen WERKT

def gemiddelde():
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    aantal = 0
    totaal = 0
    for item in lijst:
        totaal = totaal + item
        aantal = aantal + 1
    gem = totaal/aantal
    print('Gemiddelde = ',gem)


#gemiddelde()

def gemiddeldelijst():
    hoofdlijst = [[5,8,3],[5,2,6],[1,4,9,3,5],[4,3,7]]
    gemlijst = []
    for lijst in hoofdlijst:
        totaal = 0
        aantal = 0
        for getal in lijst:
            totaal = totaal + getal
            aantal = aantal + 1
        gem = totaal/aantal
        gemlijst.append(gem)
    totaal = 0
    aantal = 0
    for item in gemlijst:
        totaal = totaal + item
        aantal = aantal + 1
    antwoord = round(totaal/aantal,1)
    print('Gemiddelde = ',antwoord)

#gemiddeldelijst()

#7 Random WERKT

def random():
    import random
    getal = random.randrange(10)
    while True:
        gok = int(input('Gok een getal: '))
        if gok == getal:
            print("Goed geraden!, het was {}".format(getal))
            break
        else:
            print('Gok opnieuw!')
            continue

#random()

#8 Compressie WEKRT

def compressie():
    antwoord = ""
    bestand = open("compressie.txt" ,"r")
    data = bestand.read().split('\n') #leest data uit bestand en split het meteen in zitten en lege zinnen
    for zin in data:
        strip = zin.lstrip() #De l voor strip staat voor 'leading' dat betekend dat alle whitespace voor de tekst word verwijderd
        if strip != '': #Negeert de lege regels
            antwoord = antwoord + strip + '\n'

    nieuwbestand = open("compressieantwoord.txt", 'w+') #w+ maakt nieuw bestand aan als deze nog niet bestond
    nieuwbestand.write(antwoord)

#compressie()

#9 Cyclisch verschuiven WERKT

def verschuiven(ch,n):
    ch = str(ch)
    print("Begin = ", ch)
    antwoord = ""
    vervangen = ""
    if n == 0:# n is gelijk aan 0, zelfde waarde returnt
        print('Zelfde')
        return(ch)
    if n > 0:# n is groter dan 0, bitjes naar links
        print(n,'naar links')
        for item in ch[:n]:
            vervangen = vervangen + item
        for item in ch[n:]:
            antwoord = antwoord + item
        antwoord = antwoord + vervangen
        return(antwoord)
    if n < 0:# n is kleiner dan 0, bitjes naar rechts
        print(n,'naar rechts')
        for item in ch[n:]:
            vervangen = vervangen + item
        for item in ch[:n]:
            antwoord = antwoord + item
        antwoord = vervangen + antwoord
        return(antwoord)

ch= 1011000
n = 3
#print(verschuiven(ch,n))



#10 Fibonaci WERKT
def fibonaci(n,ans):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if len(ans) == n:
        print('Antwoord = ',max(ans))
        return(max(ans))
    else:
        ans.append(ans[len(ans)-1]+ans[len(ans)-2])


    fibonaci(n,ans) #Recursief


fibonaci(int(input("Geef een integer n: "))+1,[0,1,1]) #+1 want index begint bij 0


#11 Caesarcijfer WERKT

def caesar():
    tekst = input('Geef een tekst: ')
    stap = int(input('Geef een rotatie: '))
    antwoord = ''
    hoofd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    klein = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    """Het alfabet staat er 2 keer, dit is zodat er geen errors komen als de z bijvoorbeel 2 moet opschuiven
    (Anders zou de lijst dan out of range zijn)"""
    for letter in tekst:
        if letter in hoofd:
            index = hoofd.index(letter)
            nieuweindex = index + stap
            antwoord = antwoord + hoofd[nieuweindex]
        elif letter in klein:
            index = klein.index(letter)
            nieuweindex = index + stap
            antwoord = antwoord + klein[nieuweindex]
        else: #Voor spaties of leestekens
            antwoord = antwoord + letter
    print('Caesarcode = {}'.format(antwoord))

#caesar()

#12 FizzBuzz WERKT
def fizzbuzz():
    for item in range(1,101):
        if item%3 == 0 and item%5 ==0: #Kijkt of er een rest is na de deling
            print('fizzbuzz')
        elif item%3 == 0:
            print('fizz')
        elif item%5 == 0:
            print('buzz')
        else:
            print(item)



#fizzbuzz()






