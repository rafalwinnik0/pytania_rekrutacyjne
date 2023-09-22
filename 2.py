A = [1,2,3,3,2,1,2,3]
B = []

for i in A:
    if i not in B:
        B.append(i)
C = list(set(A))
print(B)
print(C)