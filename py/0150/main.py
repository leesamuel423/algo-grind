from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case "+":
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    stack.append(num_1 + num_2)
                case "-":
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    stack.append(num_2 - num_1)
                case "*":
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    stack.append(num_1 * num_2)
                case "/":
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    stack.append(int(num_2 / num_1))
                case _:
                    stack.append(int(i))
        return stack[0]
