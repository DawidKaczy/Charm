
lista = []
wynik = 0
for i in range(2,10,1):
    lista.append(1 - i)
print('Zbiór (1 - x) = ',lista)

lista2 = []
for i in range(0,8,1):
    lista2.append(4 ** i)
print('Zbiór B =', lista2)

lista3 = []
for i in range(len(lista2)):
    if lista2[i] % 2 == 0:
        lista3.append(lista2[i])
print('Podzielne przez 2 z listy B', lista3)

#dodaje se liczby tak o
for i in range(0,9,1):
    lista.append(i)

lista4 = []
for i in lista:
    if lista[i] % 2 == 0:
        lista4.append(lista[i])
print('Podzielne przez 2 z listy A i dodatkowe 10',lista4)

#klucz : wartosc
slownik = {'jabłka' : 'sztuki','ziemniaki' : 'kg','pomidory' : 'sztuki','cebula' : 'kg','por' : 'sztuki', }

slownik_sztuki = []
for key, value in slownik.items():
    if value == 'sztuki':
        slownik_sztuki.append(key)
print(slownik_sztuki)

def czyprostokatny(a,b,c):
    if (a*a + b*b == c*c):
        return print('Jest prostokątny')
    else:
        return print('Nie jest prostokątem')

czyprostokatny(3,4,5)

def poletrapezu(a,b,wysokosc):
    return print(1/2 * (a+b) * wysokosc)

poletrapezu(1,1,1)


import math

ok = int(input('Podaj liczbe nie ujemna = '))
if ok < 0:
    print('Błąd liczba ujemna')
else:
    print(math.radians(ok))



