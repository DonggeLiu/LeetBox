"""
Question:
https://leetcode.com/problems/longest-increasing-subsequence/description/
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def locate(l, r):
            m = (l + r) // 2
            return l if l >= r else locate(m + 1, r) if ans[m] < num else locate(l, m)

        ans = []
        for num in nums:
            if ans and num <= ans[-1]:
                ans[locate(0, len(ans))] = num
                continue
            ans.append(num)
        return len(ans)
