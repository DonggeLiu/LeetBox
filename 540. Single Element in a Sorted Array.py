

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        Succinct but requires O(n)
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

    def singleNonDuplicate(self, nums):
        """
        Requires O(logn) and less memory
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        mid = len(nums)//2
        equals = (nums[mid-1] == nums[mid])

        if mid % 2 == equals:
            return self.singleNonDuplicate(nums[mid+equals:])
        return self.singleNonDuplicate(nums[:mid-equals])
