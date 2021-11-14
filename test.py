# A
n = 1
while True:
    if 6 * (10 ** 6) * n > (10 ** 12) * 60:
        break
    n += 1
print('A: ', n - 1)

# B
n = 1
while True:
    if (10 ** 4) * (2 ** n) > (10 ** 12) * 60:
        break
    n += 1
print('B: ', n - 1)

# C
n = 1
while True:
    if (2 ** (2 ** n)) > (10 ** 12) * 60:
        break
    n += 1
print('C: ', n - 1)
