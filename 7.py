# 123456789 - Jan Kot
# 999888777 - Anna Lis
# 111222333 - Jan Lis
import sys

# krotka
K = ((123456789, 'Jan Kot'), (999888777, 'Anna Lis'), (111222333, 'Jan Lis'))

# lista
L = [(123456789, 'Jan Kot'), (999888777, 'Anna Lis'), (111222333, 'Jan Lis')]
for i in enumerate(L):
    #print(i[1][0])
    if i[1][0] == 123456789:
        print(f"Lista: {i[1][1]} and his size: {sys.getsizeof(L)}")

# słownik
S = {
    123456789: 'Jan Kot',
    999888777: 'Anna Lis',
    111222333: 'Jan Lis',
}
print(f"Słownik: {S[123456789]} and his size: {sys.getsizeof(S)}")
