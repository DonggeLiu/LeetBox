"""
Question:
https://leetcode.com/problems/spiral-matrix/
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        result = []
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = mi = 0

        for _ in range(R * C):
            result.append(matrix[r][c])
            seen[r][c] = True
            nr, nc = r + moves[mi][0], c + moves[mi][1]
            if 0 <= nc < C and 0 <= nr < R and not seen[nr][nc]:
                r, c = nr, nc
            else:
                mi = (mi + 1) % 4
                r, c = r + moves[mi][0], c + moves[mi][1]
        return result
