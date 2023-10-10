 import os

 def wypisz_zawartosc_katalogu(sciezka_do_katalogu):
     for element in os.listdir(sciezka_do_katalogu):
         sciezka_do_elementu = os.path.join(sciezka_do_katalogu, sciezka_do_elementu)
         if os.path.isdir(sciezka_do_elementu):
             wypisz_zawartosc_katalogu(sciezka_do_elementu)
         else:
             print(sciezka_do_elementu)

         