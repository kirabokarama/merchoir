# types of functions
# built in fx:  print, len, random
# user defined fx

# defining a function in py

from decimal import DivisionByZero


def divide_two_numbers(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("number 2 can't be zero")


    # if number2 != 0:
    #     return number1 / number2



# calling a fx
# print(divide_two_numbers(20, 2))
# test()
# test("hello functions")

name = "James"
