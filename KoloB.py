import math
#zad1
plikteskt = open("tekst.txt","r",encoding="utf8")
znaki71 = plikteskt.read(70)
znaki40 = plikteskt.read(40)
print(znaki40)

wynik = 0
for i in znaki40:
    if(i == "A"):  #lub dla małych islower
        print(i)
        wynik = wynik + 1

if(znaki40 == 0):
    print("Brak dużych liter 'A'")
else:
    print("Ilość dużych znaków 'A':",wynik)

#zad2 python comprehension
liczby = [2.3, 7, 13, 4.7, 8, 6.994, 10]
b = 5
nowa_lista = [liczba for liczba in liczby if isinstance(liczba, float)]
print(liczby)
print(nowa_lista)

#zad3
def sumowanie(lista1):
    listawynik = []
    for i in range(len(lista1)):
        listawynik.append(lista1[i] + lista1[0])
    return listawynik

print(sumowanie([1,2,3,4,5]))

#zad4
sin56 = math.sin(56)
log = math.log(85, 3)
dzialanie = (sin56**2) + ((4**2/25) + log)**(1/4)
dzialanie = round(dzialanie,2)
print(dzialanie)

#zad5
try:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    wynik = 0
    for i in range(a+1):
        wynik = wynik + i

    wynik2 = 0
    for x in range(b+1):
        wynik2 = wynik2 + x

    c = wynik + wynik2

    plik =open("zadanie1.txt", "w")
    plik.write(str(c))
    plik.close()
    print(c)

except:
    ValueError:print("Wprowadzona wartość nie jest liczbą całkowitą")

#lub
try:
    n1 = int(input("Podaj pierwszą liczbę całkowitą: "))
    n2 = int(input("Podaj drugą liczbę całkowitą: "))
except ValueError:
    print("Wprowadzone wartości nie są liczbami całkowitymi.")
else:
    if n1 <= 0 or n2 <= 0:
        print("Liczby muszą być dodatnie.")
    else:
        if n1 > n2:
            n1, n2 = n2, n1
        suma = sum(range(n1, n2+1))
        with open("zadanie5.txt", "w") as f:
            f.write(str(suma))
        print(f"Suma liczb od {n1} do {n2} wynosi: {suma} ")

