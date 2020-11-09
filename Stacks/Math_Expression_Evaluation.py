
#Evaluates Math Expressions
#Author: Ryan Arendt
#Implementations of the Stack, Infix, Postfix & Evauation adapted from: (IIT CS 331 Lecture)
#https://www.youtube.com/watch?v=721npTDUT9w&list=PLdrRMzNWVMEzl4G5zOlyF5BAQZ0IOFGwS&index=1

""" This program evalutates a mathematcial expression (such as: '2*8+4-12') by converting the string to a 
    list containing only digits and operators, converting that list from infix to postfix and then evaluating the
    postfix expression. This program also has the option to evaulate an algebraic expression. For example: 
    '2x+1' if x=2, evaluates to 5. The main goal of this program is to serve as a stepping stone and be used for
    a larger program to evaluate and display math equations. (Or maybe a graphing calculator program)
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


def convert_to_list(input_str): 
    """ Converts the math expression (a string) to a list containing integers (the numbers)
        and operators. This is used to convert the string before passed into the infix_to_postfix function.
    """
    math_expression = []
    cur_num = ""

    for char in input_str: 
        if is_int(char): 
            cur_num += char
        else: 
            if cur_num != "":
                math_expression.append(int(cur_num))
                cur_num = ""
                math_expression.append(char)
            else:
                math_expression.append(char)
    
    if cur_num != "": 
        math_expression.append(int(cur_num))

    return math_expression

    
def is_int(test_str): 
    """ This is a helper function to determine if a given character is an
        integer. Used in the infix_to_postfix, convert_to_list and eval_postfix functions.
    """
    try: 
        int(test_str)
        return True
    except: 
        return False


def infix_to_postfix(infix_expression): 
    """ Converts an infix mathematical expression (string) to a postfix one. The post fix expression that this 
        function returns should contain the numbers and operands of the orginal expression, just changed to postfix. 
    """
    #Note: eventually want to add the ability to handle exponents
    op_order = {"*":3, "/":3, "+":2, "-": 2, "(" :1}
    op_stack = Stack()

    postfix_list = [] 

    for char in infix_expression: 
        if is_int(char):
            postfix_list.append(char)
        elif char == "(":
            op_stack.push(char)
        elif char == ")":
            top_char = op_stack.pop()
            while top_char != "(": 
                postfix_list.append(top_char)
                top_char = op_stack.pop()
        else:    
            while(not op_stack.is_empty()) and ( op_order[op_stack.peek()] >= op_order[char]):
                postfix_list.append(op_stack.pop())

            op_stack.push(char)

    while not op_stack.is_empty(): 
        postfix_list.append(op_stack.pop())

    
    return postfix_list


def eval_postfix(postfix_list):
    """ This function evaluate a postfix expression. An an input: the postfix expression should be a list that
        contiains only integers and operators of a mathematical expression. This function does not handle floats, exponents
        and not all mathematical statements have been verified to work.
    """
    op_stack = Stack() 

    for char in postfix_list: 
        if is_int(char):
            op_stack.push(char)
        else: 
            num_2 = op_stack.pop()
            num_1 = op_stack.pop()

            result = eval_expression(char, num_1, num_2)
            op_stack.push(result)

    return op_stack.pop()


def eval_expression(op_char, a, b):
    """ This is a helper function that computes the mathematical result of two numbers. 
        This is used in the evaluate_postfix function. 
     """
    if op_char == "*":
        return a*b

    elif op_char == "/":
        return a/b

    elif op_char == "+":
        return a + b

    else: 
        return a-b


def replace_var(infix_str, var, num):
    """ Replaces the given varaible in an infix expression with the given number.
        For example: '2x+4' x: 3 becomes 2*3+4
    """
    for i in range(0, len(infix_str)): 
        if infix_str[i] == var: 
            infix_str[i] = num

    return infix_str


# eq_1 = "2*x+1"
# a = convert_to_list(eq_1)
# print(a)

# b = replace_var(a, 'x', 5)
# print(b)

# c = infix_to_postfix(b)
# print(c)

# d = eval_postfix(c)
# print(d)