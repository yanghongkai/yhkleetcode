
# 887 鸡蛋掉落 https://leetcode-cn.com/problems/super-egg-drop/


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # 缓存
        memo = dict()
        def dp(K, N):
            # base cases
            if N == 0:
                return 0
            if K == 1:
                return N
            if (K, N) in memo:
                return memo[(K, N)]

            res = float("inf")
            # 线性计算
            for i in range(1, N + 1):
                res = min(res, max(
                    dp(K-1, i-1),
                    dp(K, N-i)
                )+1)
            # 记入备忘录
            memo[(K, N)] = res
            # print(res)

            return res

        return dp(K, N)


s = Solution()
print(s.superEggDrop(2, 6))


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            # K 鸡蛋数 N楼层数
            # base case
            # 当楼层N为0，不需要扔鸡蛋
            if N == 0:
                return 0
            # 当鸡蛋为1， 只能遍历所有楼层
            if K == 1:
                return N
            if (K, N) in memo:
                return memo[(K, N)]

            res = float("inf")
            for i in range(1, N+1):
                res = min(res, max(
                    dp(K-1, i-1),  # 鸡蛋碎了
                    dp(K, N-i)  # 鸡蛋没碎
                )+1)

            memo[(K, N)] = res

            return res

        return dp(K, N)






