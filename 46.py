# importujemy kazdy modul w osobnej linii
import os
import math

# jedna linijka pustej przestrzeni między modułami różnych typów
import modul_zewnetrzny

import moj_fajny_modul

# nas klasą i pod klasą zostawiamy dwie wolne linie
# CapeCase dla nazw klas
# *
# *
class KlasyDuzymiLiterami:
    pass
# *
# *
# zmienne zawsze małymi literami, nie powinnismy uzyc znakow specjalnych ani cyfr, slowa oddzielamy _,
zmienne_malymi_literami = 'snake case'

# nad funkcją i pod funkcją zostawiamy jedną linię wolną, nazwy funkcji tworzymy tak samo
# jak nazwy zmiennych, małymi literami, oddzielając kolejne słowa _
# *
def funkcja_rowniez_malymi():
    pass
# *
# przy tworzeniu sekwencji np. list zostawiamy spacje przestrzeni pomiędzy elementami
# command+alt+L do poprawienia kodu w PyCharm
A = [1, 2, 3] # dobrze
B = ['tak','jest','niedobrze']

