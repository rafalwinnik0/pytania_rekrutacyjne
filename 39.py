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
print(Matematyka.dodaj_i_pomnoz(2,3))

 # metody działające na obiektach klasy posiadające słowo 'self'

 # metody statyczne, nie posiadają słowa kluczowego i wyglądają jak każda inna metoda

 # metody klasowe, używają słowa 'cls' i są świadome bycia wewnątrz klasy, nie potrzebują
 # obiektu danej klasy, ale wiedzą, że znajdują się wewnątrz klasy