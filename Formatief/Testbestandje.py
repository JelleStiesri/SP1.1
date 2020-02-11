def sorteren():
    lijst = [4, 3, 6, 3, 5, 7, 5, 4, 3, 2, 7, 2, 9, 5, 3, 2, 1, 2, 4, 5, 7, 3, 4, 6, 3]
    leeg = []
    leeg.append(lijst[0])
    lijst.pop(0)

    while len(lijst) > 0:
        print()



sorteren()


# uitkomst [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 9]