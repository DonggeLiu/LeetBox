"""
Question
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_dict, self.val_list = {}, []

    def insert(self, val):
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_dict:
            return False
        self.val_dict[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        val_id = self.val_dict.get(val)
        if val_id is None:
            return False
        self.val_list[val_id] = self.val_list[-1]
        self.val_dict[self.val_list[-1]] = val_id
        self.val_dict.pop(val)
        self.val_list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # print(self.val_dict, self.val_list)
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
