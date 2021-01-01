"""
Question:
https://leetcode.com/problems/super-ugly-number/
"""

from heapq import heappop, heappush


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        cur = 1
        for _ in range(n):
            cur = heappop(heap)
            for p in primes:
                heappush(heap, cur * p)
                if not cur % p:
                    break
        return cur
