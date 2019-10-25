# 134 加油站 https://leetcode-cn.com/problems/gas-station/

# 1. 随机选择一个加油站出发
# 2. 选择能到的还没去过的下一个加油站后剩下的最多的油料

# 剪枝策略:
# 1. 如果 sum(gas) < sum(cost),那么不可能环形一圈
# 1. 引入变量cur_gas, 记录当前油箱里剩余的总油量。如果在某一个加油站 cur_gas 比 0 小，意味着我们无法达到这个加油站。
# 下一步我们把这个加油站当做新的起点，并将 cur_gas 重置为0，因为重新触发，油箱中的油为0.(从上一次重置的加油站到当前加油站的任意一个加油站触发，到达当前加油站之前，cur_gas也一定会比0小)



class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        只需要进行一次遍历
        :param gas: 能获得的汽油
        :param cost: 需要消耗的汽油，先消耗，才能获得
        :return:
        """
        covered = []
        cur_gas = 0
        fail_start = []
        # 起始点i
        start = 0
        cur_gas += gas[start]
        j = start
        while cur_gas >= 0 and j<=len(gas)-1:
            # 可以到达下一个点
            if cur_gas >= cost[j]:
                cur_gas -= cost[j]
                j = (j+1) % len(cost)
                covered.append(j)
                cur_gas += gas[j]
            else:
                # 从当前节点出发
                fail_start.append(start)
                j = (j+1) % len(cost)
                start = j
                if start in fail_start:
                    break
                cur_gas = gas[j]
                covered = []
            if len(covered) == len(gas):
                print("covered:", covered)
                return covered[-1]

        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
gas = [3, 3, 4]
cost = [3, 4, 4]
s = Solution()
print(s.canCompleteCircuit(gas, cost))