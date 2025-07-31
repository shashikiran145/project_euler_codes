# Problem 12
def tri_num(i):
    num = 0
    for j in range(0, i):
        num += i
    return num
def count_divisors(n):
    count = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2  # Count both i and n/i
    if sqrt_n * sqrt_n == n:
        count -= 1  # Correct for perfect squares
    return count

def main():
    i = 1
    sum = 0
    while i > 0:
        sum += i
        d = count_divisors(sum)
        if d > 500:
            print("The tri num: ", sum)
            print("len: ", d)
            exit()
        i += 1
main()