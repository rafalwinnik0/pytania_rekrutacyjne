print(1 == True) # operator porównania wartości
print(1 is True) # operator porównania identyczności

# listy są mutowalne, nie są tymi samymi obiektami, nie są ze sobą identyczne
A = [1, 2, 3]
B = [1, 2, 3]
print(A == B) # True
print(A is B) # False

# stringi są obiektami niemutowalnymi, w pamięci może istnieć tylko jeden
# string 'kotek', wszystkie zmienne 'kotek' będą wskazywały na ten sam string w pamięci
a = 'kotek'
b = 'kotek'
print(a == b) # True
print(a is b) # True