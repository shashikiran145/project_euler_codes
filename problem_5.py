# Problem 5
def div(n):

    continue_loop = True
    while continue_loop:
        count = 0
        i = 1
        while i < 21:
            if n % i == 0:
                count += 1
            i += 1
        if count == 20:
            print(n)
            continue_loop = False
        n += 10

div(1000)