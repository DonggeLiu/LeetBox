"""
Question:
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split("/"):
            if d == ".." and stack:
                stack.pop()
            elif d not in ["", ".", ".."]:
                stack.append(d)

        return "/" + "/".join(stack)
