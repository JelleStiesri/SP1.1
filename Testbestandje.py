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
print(verschuiven(ch,n))

"""ch = str(ch)
print(ch)
ch = ch.replace("1","")
print(ch)
"""