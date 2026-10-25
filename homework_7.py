
a: int = 1
b: int = 1

for b in range(1, 11):
    for a in range(1, 11):
        print(f"{a*b:4}", end="")
        a += 1 
    print ()
    b += 1