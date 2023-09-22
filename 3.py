a = 'abcdefg'
print(a[1])
# a[1] = 'X' # string not support item assignment
# struktury mutowalne (modyfikowalne): listy i słowniki
# struktury niemutowalne (niemodyfikowalne): stringi i tuple

a_lista = list(a)
a_lista[1] = 'X'
a = "".join(a_lista)
print(a)


