"Ik heb sommige dingen samen gedaan met Max."

#1 Pyramide WERKT
def pyramide():
    hoogte = int(input("Hoe hoog is de Pyramide: "))
    for item in range(hoogte):
        print('*'*(item+1))
    for item in range(hoogte-1,0,-1):
        print('*'*(item))

#pyramide()

#2 Testcheck WERKT
def testcheck():
    string1 = input('Geef een string: ')
    string2 = input('Geef een string: ')

    index = 0

    for item1 in string1:
        try:
            if item1 == string2[index]:
                index = index + 1
        except:
            break
    index = index + 1
    print(index)

#testcheck()

#3 Lijstcheck

#a WERKT
def count(lst,nummer):
    aantal = lst.count(nummer)
    return aantal
    #print('getal: {} komt {} keer voor in de lijst'.format(nummer,aantal))
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

#5 Sorteren

def sorteren1(): #Dit is opzich een sorteer functie, maar dit is wel heel makkelijk.. ik probeer er nog 1)
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    lijst.sort()
    print(lijst)

#sorteren1()

def sorteren():
