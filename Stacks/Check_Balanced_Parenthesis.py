#Using Stacks to check if a parenthesis in a character are balance.
#Author: Ryan Arendt
#Adapted from: https://runestone.academy/runestone/books/published/pythonds3/BasicDS/ImplementingaStackinPython.html

""" This program checks to see if the parenthesis in a character string are ballanced. In this context: "ballanced" means
    every opening parenthesis should have a closing one. For example: "({[]})[]" is balanced but "({)" is not. The key to solving
    this problem is using a Stack. (Implemended here using a Python list.) Push all of the opening parenthesis to the stack, check
    closing parenthesis by sequentially popping and matching characters from the stack. If at the end of the parenthesis string
    the stack is empty, then the parenthsis match. If not, the parenethsis do not match.
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


def general_par_checker(par_string): 

    s = Stack() 
    valid_chars = "([{"

    for char in par_string: 
        if char in valid_chars: 
            s.push(char)
        else: 
            if s.is_empty():
                return False 
            else: 
                if not char_matches(s.pop(), char):
                    return False

    return s.is_empty()


def char_matches(left_paren, right_paren):
    """ Checks so see if the opening parenthsis has a closing one by checking if their indices are equal.
        This allows us to have more then one type of opening/closing parenthesis. "([{" vs. just "{"
    """
    left_symbols = "([{"
    right_symbols = ")]}"

    return left_symbols.index(left_paren) == right_symbols.index(right_paren)


#print(general_par_checker("{()}"))
#print(par_checker("(()"))