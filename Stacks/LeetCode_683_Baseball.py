
#LeetCode Problem 683: Baseball Game 
#Author: Ryan Arendt
#Verified: 10/23/2020

""" Problem Description: 
    At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
    An integer x - Record a new score of x.
    "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
    "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
    
    Return the sum of all the scores on the record
    Ex 1:)  Input: ops = ["5","2","C","D","+"]              Output: 30
    Ex 2:)  Input: ops = ["5","-2","4","C","D","9","+","+"] Output: 27

"""

class Solution:

    def  __init__(self):
        self.score_stack = []

    def calPoints(self,ops):
        """ Calculates the points of the "Baseball" game.
        """
        for char in ops: 
            if self.is_int(char):
                self.score_stack.append(int(char))
            else: 
                self.eval_operation(char)
        return self.eval_stack()


    def sum_prev_two_scores(self):
        """ Coresponds to '+' operation: Record a new score that is the sum of the previous 
            two scores. It is guaranteed there will always be two previous scores.
        """
        score_1_idx = len(self.score_stack)-1
        score_2_idx = len(self.score_stack)-2

        #The previous score (ith)
        score_1 = self.score_stack[score_1_idx]
        #The score before the previous score (ith-1)
        score_2 = self.score_stack[score_2_idx]

        new_score = score_1 + score_2

        self.score_stack.append(new_score)


    def double_prev_score(self):
        """ Coresponds to 'D' operation: Record a new score that is double the previous score. 
            It is guaranteed there will always be a previous score.
        """
        prev_score_idx = len(self.score_stack)-1
        prev_score = self.score_stack[prev_score_idx]

        cur_score = 2*prev_score

        self.score_stack.append(cur_score)

    def remove_prev_score(self):
        """ Corespnds to 'C' operation:  Record a new score that is double the previous score. 
            It is guaranteed there will always be a previous scor
        """
        self.score_stack.pop()

    def eval_operation(self,op_char):
        """ Determine what operation (+, C or D) should be executed based on the current string
        """
        if op_char == "+":
            self.sum_prev_two_scores()

        elif op_char == "D":
            self.double_prev_score()

        elif op_char == "C": 
            self.remove_prev_score()

        else: 
            print("Invalid Character: no function can be determined")


    def eval_stack(self):
        """ Determiens the sum of the stack: by popping off every value
        """
        #Note: I could just iterate through the list and sum up the values
        #but to keep with the flavor of the stack, going to treat it as such
        score_sum = 0

        while len(self.score_stack) > 0:
            cur_num = self.score_stack.pop()
            score_sum += cur_num

        return score_sum
        

    def is_int(self, op_char):
        """ Determiens if a given string is an integer or not. 
        """
        try: 
            int(op_char)
            return True 

        except:
            return False


#a = calc_points(["5","2","C","D","+"])
#sol = Solution()
#print(sol.is_int('56'))

#a = sol.calc_points(["5","2","C","D","+"])
#print(a)

#a = sol.calc_points(["5","-2","4","C","D", "9", "+", "+"])
#a = sol.calc_points(["1"])
#print(a)
