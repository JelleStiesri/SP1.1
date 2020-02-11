import math

def vier_kwadraten(getal):
    a=b=c=d = getal *0.25
    print(a,b,c,d)

    a = math.sqrt(a)
    b = math.sqrt(b)
    c = math.sqrt(c)
    d = math.sqrt(d)
    l = (a, b, c, d)
    print(l)

    return l

vier_kwadraten(54759)