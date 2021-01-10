"""
Question:
https://leetcode.com/problems/exclusive-time-of-functions/
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        threads = []
        for log in logs:
            t, e, s = log.split(":")
            t, s = map(int, (t, s))

            if e == "start":
                if threads:
                    times[threads[-1]] += s
                threads.append(t)
                times[threads[-1]] -= s
            else:
                times[threads[-1]] += s + 1
                threads.pop()
                if threads:
                    times[threads[-1]] -= s + 1
        return times
