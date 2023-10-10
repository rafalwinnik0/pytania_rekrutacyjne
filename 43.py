
P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]
#     0    1   2   3  4  5  6  7    8   9    10

szukana = 341
lewy = 0
prawy = len(P) - 1
while lewy <= prawy:
    srodkowy = (lewy + prawy) // 2
    if P[srodkowy] == szukana:
        print("znaleziono")
        break
    elif szukana > P[srodkowy]:
        lewy = srodkowy + 1
    else:
        prawy = srodkowy - 1
else:
    print("nie ma takiej liczby")
