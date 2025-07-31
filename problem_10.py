# Problem 10
def is_prime():
    number = 2
    list = []
    while number < 2000000:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            #print(number)
            list.append(number)
        number += 1
    print(list)
    print(sum(list))
#is_prime()


# Problem 10
def sum_of_primes(limit):
    # Initialize a boolean array where True represents a prime number
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers

    # Mark multiples of each prime starting from 2
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:  # If `num` is still marked as prime
            for multiple in range(num * num, limit, num):
                sieve[multiple] = False  # Mark multiples of `num` as not prime

    # Sum all numbers still marked as prime
    primes_sum = sum(i for i, is_prime in enumerate(sieve) if is_prime)
    print(primes_sum)

# Find the sum of all primes below 2 million
sum_of_primes(2000000)