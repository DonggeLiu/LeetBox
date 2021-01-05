"""
Question:
https://leetcode.com/problems/bulls-and-cows/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        s, g = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                b += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1
        c = sum([min(s.get(i, 0), g.get(i, 0)) for i in g.keys()])
        return str(b) + "A" + str(c) + "B"
