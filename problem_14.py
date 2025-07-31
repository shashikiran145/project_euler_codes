# Problem 14

def colatz(num, list):
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            list.append(num)
            colatz(num, list)
        else:
            num = (num * 3) + 1
            list.append(num)
            colatz(num, list)
    print(list)
    print(len(list))

    exit()

colatz(13, [])