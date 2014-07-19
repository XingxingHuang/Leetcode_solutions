# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # helper function, check if element from list is integer
    def isInt(self, x):
        try:
            int(x)
            return True
        except ValueError:
            return False

	# helper function, perform calculation		
    def operation(self, operator, number1, number2):
        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
        else:
            return int(float(number1) / number2)
			
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        numbers = []
        for x in tokens:
            if self.isInt(x):
                numbers.append(int(x))
            else:
                number2 = numbers.pop()
                number1 = numbers.pop()
                numbers.append(self.operation(x,number1,number2))
        return numbers.pop()