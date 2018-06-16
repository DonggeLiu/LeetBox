"""
Question:
https://leetcode.com/problems/top-k-frequent-elements/description/
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [num[0] for num in Counter(nums).most_common(k)]
