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
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

hundreds = {
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
}
scales= ["hundred and", "thousand"]


def two_digit(n):
    count = 0
    quotient = n // 10
    remainder = n % 10
    quotient = quotient * 10
    print(tens[quotient])
    print(single_digits[remainder])
    count += len(single_digits[remainder])
    count += len(tens[quotient])
    return count
def number():
    count = []
    n = 1
    while n < 1000:
        if n in single_digits:
            count.append(len(single_digits[n]))
            print(single_digits[n])
        elif n in tens:
            count.append(len(tens[n]))
            print(tens[n])
        elif n in teens:
            count.append(len(teens[n]))
            print(teens[n])
        elif len(str(n)) == 2 and n not in tens and n not in teens:
            count.append(two_digit(n))
        elif len(str(n)) == 3:
            if n in hundreds:
                count.append(len(hundreds[n]))
            else:
                quotient = n // 100
                remainder = n % 100
                quotient = quotient * 100
                count.append(len(hundreds[quotient])+3)
                if remainder in single_digits:
                    count.append(len(single_digits[remainder]))
                    print(single_digits[remainder])
                elif remainder in tens:
                    count.append(len(tens[remainder]))
                    print(tens[remainder])
                elif remainder in teens:
                    count.append(len(teens[remainder]))
                    print(teens[remainder])
                elif len(str(remainder)) == 2 and remainder not in tens and remainder not in teens:
                    count.append(two_digit(remainder))

        n += 1
    print(count)
    print(sum(count))


number()

# Manually added for n = 1000
