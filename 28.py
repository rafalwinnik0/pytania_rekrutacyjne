import random
A = [random.randint(0, 100) for i in range(5)]
B = [random.randint(0, 100) for i in range(5)]
H = [random.randint(0, 100) for i in range(5)]

# Vmax = 0
# liczba_iteracji = 0
#
# for a in A:
#     print()
#     for b in B:
#         print()
#         for h in H:
#             liczba_iteracji += 1
#             pole = a*b*h
#             print(f"Pole: {pole}, A,B,H: {a}, {b}, {h}")
#             if pole > Vmax:
#                 Vmax = pole
# print(Vmax)
# print(liczba_iteracji)

print(max(A)*max(B)*max(H))

