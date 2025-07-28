# Problem 3
def is_prime(iterr):
    for i in range(2, int(iterr**0.5)+1):
        if iterr % i == 0:
            return False
    return True


def large_prime(num):
    n = 2
    while n*n <= num:
        if num % n == 0:
            if is_prime(n):
                print(n)
        n += 1


large_prime(600851475143)

