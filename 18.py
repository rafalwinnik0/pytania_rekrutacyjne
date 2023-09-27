import sys
A = [4, 5, 7, -3, 2, 8, -10, 15]

# 1
# sortowanie listy, wzięcie skrajnych elementow
# A.sort() # duża złożoność obliczeniowa, O(N*log_N)
# różnica = A[-1] - A[0]
# print(różnica)

# 2
# najmniejsza = A[0]
# największa = A[0]
#
# for liczba in A:              # O(N)
#     if liczba < najmniejsza:
#         najmniejsza = liczba
#     elif liczba > największa:
#         największa = liczba
# print(największa-najmniejsza)

# 3
print(max(A) - min(A))          # O(N)