# Problem 6
def division():
    n = 2
    while n < 10:
        i = 2
        while i < 100:
            if n >= i and n % i == 0:
                print(n)
                #print(i)
                i += 1
            else:
                n += 1

division()