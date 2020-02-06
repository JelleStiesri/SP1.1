def compressie():
    antwoord = ""
    bestand = open("compressie.txt" ,"r")
    data = bestand.read().split('\n') #leest data uit bestand en split het meteen in zitten en lege zinnen
    for zin in data:
        strip = zin.lstrip() #De l voor strip staat voor 'leading' dat betekend dat alle whitespace voor de tekst word verwijderd
        if strip != '': #Negeert de lege regels
            antwoord = antwoord + strip + '\n'


    print(antwoord)
    nieuwbestand = open("compressieantwoord.txt", 'w+') #w+ maakt nieuw bestand aan als deze nog niet bestond
    nieuwbestand.write(antwoord)

compressie()
