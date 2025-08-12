def divide(number):
    n = 1
    arr = []
    while n <= (number/2):
        if number % n == 0:
            arr.append(n)
        n += 1
    return sum(arr)


def main(number):
    n = 0
    diction = {}
    addo = []
    while n <= number:
        diction[n] = divide(n)
        n += 1
    for a, b in diction.items():
        if b in diction and diction[b] == a and a != b:
            print(a, b)
            if a+b in addo:
                pass
            else:
                addo.append(a+b)

    print(sum(addo))


main(10000)







