"""
Question:
https://leetcode.com/problems/complex-number-multiplication/
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def convert(x):
            i, j = x.split("+")
            return complex(int(i), int(j[:-1]))

        result = convert(a) * convert(b)
        return str(int(result.real)) + "+" + str(int(result.imag)) + "i"
