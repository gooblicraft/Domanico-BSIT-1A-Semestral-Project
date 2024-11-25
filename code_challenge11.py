#Code Challenge 11 by Domanico

for x in range(1, 4):
    for a in range(4, x, -1):
        print(" ", end = " ")
    for b in range(0, x):
        print("*", end = " ")
    for c in range(1, x):
        print("*", end = " ")
    print()

for y in range(0,7):
    print("*", end = " ")
print()

for z in range(1, 4):
    for d in range(0, z):
        print(" ", end = " ")
    for e in range(4, z, -1):
        print("*", end = " ")
    for f in range(4, z + 1, -1):
        print("*", end = " ")
    print()