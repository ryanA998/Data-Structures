#Converts numbers from base 10 to other bases.
#Author: Ryan Arendt

""" This program can be used to convert an integer from base 10 (number system that were used to) to either
    base 2 (binary) or any other valid base. In our case: a valid base is any base that is less than or
    equal to the base ten number.
        Ex. 1) Input: 15 Output: (base 2) 1111
        Ex. 2) Input" 15 Output: (base 4) 33
        Ex. 3) Input" 15 Output: (base 5) 30
"""

class Stack: 

    def __init__(self):
        self._items = []

    def is_empty(self): 
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def disp(self): 
        print(self._items)


def base_2_converter(decimal_num): 
    """ Converts a number (int) from base 10 to base 2 (string). For example the integer 13 should 
        return the binary string: 1101.
    """
    remainder_stack = Stack() 
    binary_string = ""

    while decimal_num > 0: 

        cur_remainder = decimal_num % 2
        remainder_stack.push(cur_remainder)

        decimal_num = decimal_num // 2

    while not remainder_stack.is_empty(): 
        binary_string = binary_string + str(remainder_stack.pop())

    return binary_string


def convert_to_base(decimal_num, base): 
    """ Convers a number from base 10 (int) to another valid base. Here a valid base is one that
        is less than or equal to the original decimal number. The function should return a string reprentation
        of the original number in the coresponding base.
        Ex.1)   Input: 28   (base: 16)      Ouput: 1c
        Ex.2)   Input: 19   (base: 5)       Output: 34
    """
    converted_number = ""
    valid_digits = "0123456789ABCDEF"

    remainder_stack = Stack() 

    while decimal_num > 0: 
        cur_remainder = decimal_num % base
        remainder_stack.push(cur_remainder)
        decimal_num = decimal_num // base 

    while not remainder_stack.is_empty():
        converted_number = converted_number + valid_digits[remainder_stack.pop()]

    return converted_number


#print(convert_to_base(28, 16))