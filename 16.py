a = "python_moj_kod.py"
b = "python_notatki.txt"

def sprawdz(nazwa_pliku):
    if nazwa_pliku[:6] == 'python' and nazwa_pliku[-3:] == '.py':
        return True
    else:
        return False

print(sprawdz(a))
print(sprawdz(b))