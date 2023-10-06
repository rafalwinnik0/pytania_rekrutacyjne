# init to konstruktor klasy w pythonie, jest to metoda klasy, która pozwala tworzyć obiekty danej klasy.

class Pies():
    def __init__(self, imie, rasa):
        self. imie = imie
        self.rasa = rasa

maly_pies = Pies('Pikuś', 'ratlerek')
duzy_pies = Pies('Killer', 'doberman')

print(maly_pies.imie, maly_pies.rasa)
print(duzy_pies.imie, duzy_pies.rasa)