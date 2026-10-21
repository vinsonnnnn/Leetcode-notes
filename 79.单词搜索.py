# DFS + 当前路径访问集合


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # 第一步：记录网格尺寸、单词长度，准备当前路径访问集合
        rows, cols = len(board), len(board[0])
        length = len(word)
        visited = set()

        def dfs(r, c, index):

            # 第二步：越界、当前路径已用过或字符不匹配，直接失败
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if (r, c) in visited or board[r][c] != word[index]:
                return False

            # 第三步：当前字符已匹配，若是最后一位则整个单词成功
            if index == length - 1:
                return True

            # 第四步：接纳当前格子，防止后续路径重复使用
            visited.add((r, c))

            # 第五步：搜索四邻居，返回前撤销本格标记，成功失败都恢复
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )
            visited.remove((r, c))
            return found

        # 第六步：枚举全部起点，任一成功就结束，全部失败才返回False
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
