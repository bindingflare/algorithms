# Problem 2812 - Find the Safest Path in a Grid
# src: leetcode daily question
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid) # square grid
        if n == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = [[float('inf')] * n for _ in range(n)]

        queue = deque()
        
        # multi-source BFS
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < n:
                    if distance[ni][nj] > distance[i][j] + 1:
                        distance[ni][nj] = distance[i][j] + 1
                        queue.append((ni, nj))
        
        # BFS (0,0) to (n-1, n-1)
        max_safeness = [[-float('inf')] * n for _ in range(n)]
        max_safeness[0][0] = distance[0][0]

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < n:
                    new_safeness = min(max_safeness[i][j], distance[ni][nj])
                    if new_safeness > max_safeness[ni][nj]:
                        max_safeness[ni][nj] = new_safeness
                        queue.append((ni, nj))


        
        return max_safeness[n-1][n-1]
        

        # Example usage
example_grid = [[1,0,0],[0,0,0],[0,0,1]]

sol = Solution()
print(sol.maximumSafenessFactor(example_grid))
