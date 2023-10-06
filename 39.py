class Matematyka:

    def __init__(self):
        self.pi = 3.14

    def policz_obwod(self, r):
        return 2 * self.pi * r
    @staticmethod
    def dodaj(a, b):
        return a + b
    @classmethod
    def dodaj_i_pomnoz(cls, a, b):
        return cls.dodaj(a, b) * 2

m = Matematyka()
print(m.policz_obwod(5))
print(Matematyka.dodaj(2,3))

