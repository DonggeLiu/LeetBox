class Solution(object):

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        char_index = {c:i for i, c in enumerate(S)}
        ans = []
        counter = anchor = 0

        for i, c in enumerate(S):
            counter = max(counter, char_index[c])

            if i == counter:
                ans.append(counter+1 - anchor)
                anchor = counter+1
                counter = 0

        return ans
