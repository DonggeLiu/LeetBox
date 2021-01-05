class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        ends = {p[0]: 1}
        lasts = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1]) == 1) or (p[i] == 'a' and p[i - 1] == 'z'):
                lasts += 1
            else:
                lasts = 1
            ends[p[i]] = max(lasts, ends.get(p[i], 0))

        return sum(ends.values())
