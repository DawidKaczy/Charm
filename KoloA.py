import math
# zad1
# try:
#     a = int(input("Podaj a: "))
#     b = int(input("Podaj b: "))
#
#     c = (a**2)+(a*b)+(b**2)
#
#     plik =open("zadanie1.txt", "w")
#     plik.write(str(c))
#     plik.close()
#     print(c)
#
# except:
#     ValueError:print("Wprowadzona wartość nie jest liczbą całkowitą")

#zad 2
def tworzenieListy(lista1, lista2):
    listaWynik = []
    for i in range(min(len(lista1), len(lista2))):
        listaWynik.append(lista1[i] + lista2[i])
    return listaWynik

print(tworzenieListy([1,2,3,4],[2,2,2,2,2]))

#zad 3
plikteskt = open("tekst.txt","r",encoding="utf8")
znaki100 = plikteskt.read(99)
znaki35 = plikteskt.read(35)
print(znaki35)

wynik = 0
for i in znaki35:
    if i.isupper():  #lub dla małych islower
        print(i)
        wynik = wynik + 1

if(znaki35 == 0):
    print("Brak dużych liter")
else:
    print("Ilość dużych znaków:",wynik)

#zad4
lista = [2, 7, 13, 4, 8, 6, 10]
a = 5
listawynik = []
for i in range(len(lista)):
    if(lista[i] > a):
        listawynik.append(lista[i])
print(listawynik)

#zad4 python comprehension
liczby = [2, 7, 13, 4, 8, 6, 10]
b = 5
nowa_lista = [liczba for liczba in liczby if liczba > a]
print(nowa_lista)

#zad5
e = math.e
pi = math.pi
cos39 = math.cos(39)

wynik = ((e**3 + cos39**2)**(1/5)) + ((2/7)**3) + pi
wynik = round(wynik, 2)

print(wynik)
