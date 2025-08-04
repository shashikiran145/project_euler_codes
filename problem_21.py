def ami(num):
    n = 1
    arr = []
    while n <= (num/2):
        if num % n == 0:
            arr.append(n)
        n += 1
    #print(arr)
    return sum(arr)

# def main(number):
#     n = 0
#     sum_arr = []
#     while n <= number:
#         if ami(n) == number:
#             sum_arr.append(number)
#         else:
#             print("Numbers not found")
#         n += 1
#     print(sum_arr)

print(ami(10))
#main(284)





