# 分层多源BFS
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 第一步：处理空网格，获取行数和列数
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        # 第二步：准备队列、新鲜橘子数和四个方向
        queue = deque()
        fresh = 0
        direcations = ((1, 0), (0, 1), (-1, 0), (0, -1))

        # 第三步：所有初始腐烂源入队，同时统计新鲜数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        # 第四步：没有新鲜橘子就返回0；否则逐层模拟时间
        if fresh == 0:
            return 0
        minutes = 0

        while queue and fresh > 0:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()

                # 第五步：感染四邻新鲜橘子，立即标记并留到下一轮传播
                for dr, dc in direcations:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            # 当前时间层全部传播完，经过一分钟
            minutes += 1

        # 第六步：新鲜橘子清零则返回时间，否则存在不可达橘子
        return minutes if fresh == 0 else -1
