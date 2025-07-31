# Problem 9
def py_triplets():
    for a in range(1,1000):
        for b in range(a+1, 1000-a):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                print(f"{a}, {b}, {c}")
                print(a*b*c)
py_triplets()