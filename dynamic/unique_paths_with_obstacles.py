
# 63 不同路径II https://leetcode-cn.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """

        :param obstacleGrid:
        :return:
        """
        # m 表示列， n表示行
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        cell = [[0]*m for i in range(n)]
        if not obstacleGrid[0][0]:
            cell[0][0] = 1
        for i in range(n):
            for j in range(m):
                if not (i==0 and j==0):
                    if obstacleGrid[i][j] == 1:
                        cell[i][j] = 0
                    else:
                        cell[i][j] = (cell[i-1][j] if i>=1 else 0)  + (cell[i][j-1] if j>=1 else 0)
        return cell[-1][-1]


obstacle_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
obstacle_grid = [
    [1]
]
s = Solution()
print(s.uniquePathsWithObstacles(obstacle_grid))



