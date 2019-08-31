class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        h = [max(street) for street in grid]
        v = [max([street[i] for street in grid]) for i in range(len(grid))]
        count = 0
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                count += min(h[k],v[j]) - grid[j][k]
        return count

# Runtime: 32 ms
# Memory Usage: 13.3 MB