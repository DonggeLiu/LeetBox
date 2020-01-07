"""
Question
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        op = "+"
        s += "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c != " ":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(num * -1)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                op = c
        return sum(stack)
