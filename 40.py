# n % 3 == 0 -> FIZZ
# n % 5 == 0 -> BUZZ
# n % 3 == 0 and n % 5 == 0 -> FIZZBUZZ

# def fizzbuzz(n):
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FIZZBUZZ")
#         elif i % 3 == 0:
#             print("FIZZ")
#         elif i % 5 == 0:
#             print("BUZZ")
#         else:
#             print(i)
#
# fizzbuzz(15)

def fizzbuzz(n):
    for i in range(1, n+1):
        wynik = ''
        if i % 3 == 0:
            wynik += 'FIZZ'
        if i % 5 == 0:
            wynik += 'BUZZ'
        if i % 3 != 0 and i % 5 != 0:
            wynik = i
        print(wynik)

fizzbuzz(15)