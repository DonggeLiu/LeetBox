"""
Question:
https://leetcode.com/problems/longest-absolute-file-path/
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dir_dict = defaultdict(lambda: 0)
        max_len = 0
        for line in input.splitlines():
            file, level = line.lstrip("\t"), line.count("\t")
            if "." in file:
                max_len = max(max_len, dir_dict[level - 1] + len(file))
            else:
                dir_dict[level] = dir_dict[level - 1] + 1 + len(file)
        return max_len
