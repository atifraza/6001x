num = 6
#L = [5, 0, 2, 4, 6, 3, 1]
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val