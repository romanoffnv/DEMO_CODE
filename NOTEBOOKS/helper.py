import random
L = [random.randint(1, 20) for x in range(10)]
var = 0

for i in range(1, len(L)):
    var = i
    for j in L[0:var]:
        print(j)
    # print(L[i] < L[i - 1])