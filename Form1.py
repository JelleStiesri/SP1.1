#1
#?

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

#2 Lijstcheck

#a
def count():
    lijst = [4,3,6,3,5,7,5,4,3,2,7,2,9,5,3,2,1,2,4,5,7,3,4,6,3]
    nummer = int(input('Welk nummer wil je tellen?: '))
    aantal = lijst.count(nummer)
    print('getal: {} komt {} keer voor in de lijst'.format(nummer,aantal))
#b
def verschil():
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    index = 1
    for item in list 

verschil()