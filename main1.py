import math

euler = math.e
wynik = euler ** 10
print("Euler do potegi 10 = ", wynik)


kat = 8
sinus = math.sin(math.radians(8))
sinusdo2 = sinus ** 2
wynik2 = math.log(5 + sinusdo2)
wynik3 = wynik2 ** 1/6
print("Wynik = ", wynik3)

x = 3.55
ok = int(x)
print("Część całkowita = ", ok)

ok2 = math.ceil(x)
print(ok2)

imie = 'DAWID'
nazwisko = 'KACZYNSKI'

print(imie.capitalize())
print(nazwisko.capitalize())

piosenka='Jolka, Jolka, Jolka czy pamiętasz'
print("Ile Jolek? =", piosenka.count('Jolka'))

tekst = 'Kotek'
print("Wyświetl 2 literę =", tekst[1])
print("Wyświetl ostatnią literę =", tekst[-1])

print('Podzielenie =', piosenka.split())

napis = "Hello, World!"
liczba_zmiennoprzecinkowa = 3.14159
liczba_hex = 0x1a

print(f"{napis}")
print(f"{liczba_zmiennoprzecinkowa:.2f}")
print(f"0x{liczba_hex:X}")


lista =['piłka nożna','siatkówka','koszukówka']
lista.reverse()
lista.append('klocki lego')
print(lista)

slownik = {'ok': 'okej','np' : 'na przykład','btw':'by the way'}
print(slownik['ok'])

slownik2 = {1: 'CS', 2 : 'LOL', 3:'DOTA',4 :'COD'}
print("Ilość gier = ", len(slownik2))

# ilosc = input("Napisz coś = ")
# print("ilosc a= ", ilosc.count('a'))  liczy ile a

# num = int(input("Podaj 1 liczbę całkowitą: "))
# num2 = int(input("Podaj 2 liczbę całkowitą: "))
# num3 = int(input("Podaj 3 liczbę całkowitą: "))
#
# if num > num2 and num > num3:
#     print(num)
# elif num2 > num and num2 > num3:
#     print(num2)
# else:
#     print(num3)

tab = [1, 2, 3, 5.6, 4.3, 4,5]

for i in range(len(tab)):
    tab[i] = tab[i] ** 2

print(tab)

liczby_parzyste = []

i = 0
while i < 10:
    liczbapo = int(input("Podaj liczbę: "))
    if liczbapo % 2 == 0:
        liczby_parzyste.append(liczbapo)
    i += 1

print("Liczby parzyste: ", liczby_parzyste)

