#
# # Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku
# lista = []
# for i in range(11):
#     lista.append([i * 2])
#
# plik = open("dane.txt","a+")
# plik.writelines(str(lista))
# #zamknięcie pliku
# plik.close()
#
# # Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
# plik = open("dane.txt","r")
# #odczyt jednej lini z pliku
# linia = plik.readline()
# #zamknięcie pliku
# plik.close()
# #drukujemy linie
# print(linia)



with open('dane.txt','r') as plik:
    for linia in plik:
        print(linia, end="")




