"""
Question
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
