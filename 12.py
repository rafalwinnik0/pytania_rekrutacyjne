jezyki = ['Python', 'Java', 'C#', 'Ruby']

# 1
# jezyki.reverse()
# jezyki_odwroceone = jezyki
# print(jezyki_odwroceone)

# 2
# jezyki_odwrocone = list(reversed(jezyki))
# print(jezyki_odwrocone)

# 3
# jezyki_odwrocone = jezyki[::-1]
# print(jezyki_odwrocone)

# 4
jezyki_odwrocone = []
for jezyk in jezyki:
    jezyki_odwrocone.insert(0,jezyk)
print(jezyki_odwrocone)
