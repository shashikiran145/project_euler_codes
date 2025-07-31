# Problem 4
def is_palindrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        print(number)
        return True
    else:
        return False


# Problem 4
def mul():
    list = []
    for n in range(999, 100, -1):
        for i in range(999, 100, -1):
            product = n * i
            if is_palindrome(product):
                list.append(product)
                break
    print(sorted(list))
mul()