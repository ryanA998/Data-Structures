#Using a Stack to convert an expression from Infix to Postfix
#Author: Ryan Arendt
#Algorithem adapted from: 
#https://runestone.academy/runestone/books/published/pythonds3/BasicDS/InfixPrefixandPostfixExpressions.htm

""" This program uses a stack to convert an infix expression (string) to a postfix expression (string). Remember an infix expression
    can be though of as writting a expression like we are used to: '( A + B ) * C' and an postfix expression has the math operators
    written on the outside: A B + C *
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


def infix_to_postfix(infix_expr):
    """ Converts an infix_expression (string) and returns a postfix expression (string). 
        Note: this method assume that the only valid parenthesis are '(' and ')'
    """
    prec = {"*":3, "/":3, "+": 2, "-":2, "(":1}
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_digits = "0123456789"

    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
    
        if token in valid_characters or token in valid_digits:
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


# b = infix_to_postfix("( A + B ) * C")   
# print(b)