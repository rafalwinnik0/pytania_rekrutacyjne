# assert - uznanie zdania za prawdziwe
def dodawanie(a,b):
    return a+b

def test_intow():
    assert dodawanie(2,3) == 5

def test_stringow():
    assert dodawanie('a','b') == 'ab'

# pytest sprawdza funkcje, które mają w nazwie na początku test

