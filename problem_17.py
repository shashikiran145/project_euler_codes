single_digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
teens = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
tens = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
scales= ["hundred and", "thousand"]


def two_digit(number):
    elif len(str(n)) == 2:
    if n in tens:
        count.append(len(tens[n]))
        print(tens[n])
    elif n in teens:
        count.append(len(teens[n]))
        print(teens[n])
    else:
        quotient = n // 10
        remainder = n % 10
        quotient = quotient * 10
        print(tens[quotient])
        print(single_digits[remainder])
        count.append(len(single_digits[remainder]))
        count.append(len(tens[quotient]))
def number():
    count = []
    n = 1
    while n < 1000:
        if len(str(n)) == 1:
            remainder = n % 10
            print(single_digits[remainder])
            count.append(len(single_digits[remainder]))
        elif len(str(n)) == 2:
            if n in tens:
                count.append(len(tens[n]))
                print(tens[n])
            elif n in teens:
                count.append(len(teens[n]))
                print(teens[n])
            else:
                quotient = n // 10
                remainder = n % 10
                quotient = quotient*10
                print(tens[quotient])
                print(single_digits[remainder])
                count.append(len(single_digits[remainder]))
                count.append(len(tens[quotient]))
        elif len(str(n)) == 3 and n < 105:
            if n in tens:
                count.append(len(tens[n]))
                print(tens[n])
            elif n in teens:
                count.append(len(teens[n]))
                print(teens[n])
            else:
                quotient = n // 10
                remainder = n % 10
                quotient = quotient*10
                print(tens[quotient])
                print(single_digits[remainder])
                count.append(len(single_digits[remainder]))
                count.append(len(tens[quotient]))
        else:
            break

        n += 1
    print(count)
    #print(sum(count))


number()


