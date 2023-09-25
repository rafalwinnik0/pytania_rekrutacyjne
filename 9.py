x = 'myszydokazujągdykotanieczują'
print(len(x))
dict = {}

for index, letter in enumerate(x):
    if letter not in dict:
        dict[letter] = 1
    else:
        dict[letter] += 1

print(dict)


