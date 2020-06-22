
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
            # for i in range(1, N + 1):
            #     res = min(res, max(
            #         dp(K-1, i-1),
            #         dp(K, N-i)
            #     )+1)

            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                # 碎
                broken = dp(K-1, mid-1)
                # 不碎
                not_broken = dp(K, N-mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            # 记入备忘录
            memo[(K, N)] = res
            # print(res)

            return res

        return dp(K, N)


s = Solution()
print(s.superEggDrop(2, 6))






