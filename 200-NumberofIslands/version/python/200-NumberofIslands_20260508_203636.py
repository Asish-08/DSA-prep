# Last updated: 5/8/2026, 8:36:36 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1
        
        return islands
                
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        grid[r][c] = '0' # mark current index seen

        # check each direction
        lst = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        for row, col in lst:
            # check bounds and if next is an island
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid, row, col)

        return
