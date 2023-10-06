class Pies():
    def __init__(self, imie, rasa):
        self. imie = imie
        self.rasa = rasa

    def __str__(self):
        return f"Imie: {self.imie}, rasa: {self.rasa}"

maly_pies = Pies('Pikuś', 'ratlerek')

print(maly_pies)