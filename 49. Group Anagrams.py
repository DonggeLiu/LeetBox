"""
Question
https://leetcode.com/problems/group-anagrams/description/
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = {}
        for word in strs:
            word_key = ''.join(sorted(word))
            if word_key in anagrams_dict:
                anagrams_dict.get(word_key).append(word)
            else:
                anagrams_dict[word_key] = [word]
        return list(anagrams_dict.values())
