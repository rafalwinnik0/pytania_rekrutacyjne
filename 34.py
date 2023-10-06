# generatory w pyhonie są rodzajem funkcji, która zwraca obiekt będący iteratorem, iterator
# jest to obiekt, po którym możemy iterować, czyli odbierać po jednej wartości z danego obiektu
# za każdym razem
# aby użyć generatora trzeba utworzyć obiekt generatora
def zwracaj_kolejne_parzyste():
    for n in range(2,20,2):
        yield n

z = zwracaj_kolejne_parzyste()

# for i in range(9):
#     print(next(z))

y = ('a' * n for n in range(5))

for i in range(5):
    print(next(y))