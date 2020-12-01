"""
basic loops
"""


for number in range(101):
    if number % 3 == 0 and number % 5 ==0:
        print("fizzbuzz")
    if number %3 ==0:
        print("fizz")
        continue
    if number % 5 == 0:
        print("buzz")
        continue
    if number % number == 0 and number % 1 == 0:
        print("prime")


    print(number)




"""
EZEBUIRO UCHECHUKWU VINCENT
"""
