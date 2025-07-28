# Problem 2
def fibonacci(n):
    temp_1 = 1
    temp_2 = 2
    value = 0
    for i in range(1, n+1):
        if i == 1:
            print(temp_1)
        elif i == 2:
            print(temp_2)
        else:
            summ = temp_1 + temp_2
            if summ > 4000000:
                print(i)
                break
            temp_1 = temp_2
            temp_2 = summ
            print(summ)
            if summ % 2 == 0:
                value += summ
    print(value)


fibonacci(33)

