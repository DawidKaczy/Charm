a ='napis'
print(a)

b = 5
c = 5.5
print(b, c)

d = 5+5j
print(d)

e = b + c
print(e)

f = b**2
print(f)
# lub (potegi)
g = pow(5, 2)
print(g)

b +=2
print(b)

listy = ['a','b,',4,5,6,[1,2,3],6]
print(listy)
listy.append(4)
print(listy)
print(listy[1])

#dodat elementy na wybranej miejscu
#usunecie elementu z listy danej pozycji
#usuniecie elemntu z listy o danej wartosci
#usuniecie elementy listy
#zrobic sortowanie

listy2 = ['ok1','ok2','ok3','ok4']
print(listy2)
listy2.insert(2,6) #po index2 dodajemy 6
print(listy2)

#Usuń 4 element:
listy2.pop(3)
print(listy2)

#Usuwanie po nazwie
listy2.remove('ok1')
print(listy2)

numery = [1,2,4,3,2,7,8,4,2]
numery.sort() #sortowanie rosnaco
print(numery)

numery.sort(reverse = True) #malejaco
print(numery)

slownik = {'a': 2,1 : 2,2:'ab'}
print(slownik)
print(slownik[2])
slownik['klucz']='wartosc'
print(slownik)
slownik.pop('klucz')
print(slownik)


napis = 'a={}, b={}'
print(napis.format(12,12))
#lub
print('a={}, b={}'.format(12,12))

#if warunek
   #instrukcja1
   #instrukcja2
#elif warunek2
   #instrukcja1
   #instrukcja2
#else
   #instrukcje


# a = input('podaj a')
# b = input('podaj b')
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))
#
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print('a rowne b')
#
# if a==b:
#     print("sa rowne")
# else:
#     print('nie sa rowne')



# a = input('podaj a')
# b = input('podaj b')
# c = input('podaj c')
# d = input('podaj d')
#
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
#
# if a>b & c>d:
#     print('a wieksze od b i c wieksze od d')
# else:
#     print('a jest mniejsze od b lub c kest wieksze od d')

for x in range(1, 6, 1):
    print(x)
else:
    print('koniec petli for')

for x in listy:
    print(x)



for i in range(0, len(listy),1):
    print(listy[i])

#while

# licznik = 0
# while licznik !=len(listy):
#     print(listy[licznik])
#     licznik += 1

# liczby2 = [3,4,5,1,7,8]
# a = int(input('podaj a'))
# licznik = 0
# while licznik != len(liczby2):
#     if a - liczby2[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby2[licznik]))
#         break
#         licznik +=1

liczby2 = [1,2,2,2,3,4]
licznik = 0
while licznik != len(liczby2):
    if liczby2[licznik] == 2:
        liczby2.pop(licznik)
    else:
        licznik += 1
print(liczby2)





