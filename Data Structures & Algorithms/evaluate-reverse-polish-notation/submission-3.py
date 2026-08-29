import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Edge case
        if len(tokens) == 1:
            return int(tokens[0])

        # Use stack to keep track of latest operands 
        operandStack = []
        for item in tokens: 
            if item not in ("+", "-", "*", "/"): 
                # Its an operand 
                operandStack.append(item)
            else: 
                # Its an operator, fetch the relevant operands
                rightOperand = int(operandStack.pop())
                leftOperand = int(operandStack.pop()) 

                # Perform the computation 
                computedResult = 0 
                match item: 
                    case "+": 
                        computedResult = leftOperand + rightOperand
                    case "-":
                        computedResult = leftOperand - rightOperand
                    case "*":
                        computedResult = leftOperand * rightOperand
                    case "/": 
                        tempResult = leftOperand / rightOperand
                        # If negative, round up towards 0 
                        if tempResult < 0: 
                            computedResult = math.ceil(tempResult)
                        # If positive, round down towards 0 
                        else:
                            computedResult = math.floor(tempResult)

                operandStack.append(computedResult)

        # Since its always a valid expression
        # Stack should have one item left only at the end; evaluated output
        return operandStack[-1]




10 + (((6 / ((9 + 3) * -11)) * 17) + 5) 