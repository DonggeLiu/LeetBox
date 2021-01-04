"""
Question:
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""


class Solution:
    def originalDigits(self, s: str) -> str:
        char_dict = {c: s.count(c) for c in ascii_lowercase}

        result = [0] * 10
        result[0] = char_dict['z']
        result[2] = char_dict['w']
        result[4] = char_dict['u']
        result[6] = char_dict['x']
        result[8] = char_dict['g']

        result[1] = char_dict['o'] - result[0] - result[2] - result[4]
        result[3] = char_dict['h'] - result[8]
        result[5] = char_dict['f'] - result[4]
        result[7] = char_dict['s'] - result[6]
        result[9] = char_dict['i'] - result[5] - result[6] - result[8]

        return "".join(str(i) * result[i] for i in range(10))
