#Code Challenge 13 by Domanico

for x in range(1, 6):
    for a in range(6, x, -1):
        print(" ", end = " ")
    for b in reversed(range(1, x+1)):
        print(b, end = " ")
    for c in range(2, x+1):
        print(c, end = " ")
    print()

for z in range(4, 0, -1):
    for d in range(6, z, -1):
        print(" ", end=" ")
    for e in range(z, 0, -1):
        print(e, end=" ")
    for f in range(2, z + 1):
        print(f, end=" ")
    print()  
