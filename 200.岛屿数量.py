# 迭代DFS
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 第一步：处理空网格，获取行数和列数
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        # 第二步：准备访问集合、四方向偏移和岛屿计数
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        islands = 0

        # 第三步：扫描网格，发现未访问陆地时，新增一座岛
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1" or (r, c) in visited:
                    continue
                islands += 1
                # 第四步：起点入栈时就标记，避免被邻居重复加入
                stack = [(r, c)]
                visited.add((r, c))

                # 第五步：DFS探索并标记这座岛的全部陆地
                while stack:
                    current_r, current_c = stack.pop()
                    for dr, dc in directions:
                        nr, nc = current_r + dr, current_c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
        return islands
