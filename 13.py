def sprawdz(slowo):
    return True if slowo == slowo[::-1] else False
    # slowo_odwrocone = slowo[::-1]
    # if slowo == slowo_odwrocone:
    #     return True
    # else:
    #     return False

print(sprawdz('kajak'))
print(sprawdz('anakonda'))