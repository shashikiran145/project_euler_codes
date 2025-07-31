# Problem 7
def is_prime():
    number = 2
    count = 0
    while count < 10001:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)
            count += 1
        number += 1
is_prime()