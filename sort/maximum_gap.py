
# 最大间距 https://leetcode-cn.com/problems/maximum-gap/


class Solution:
    def maximumGap(self, nums):
        """
        先进行排序(快排)
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return 0
        # self.quick_sort(nums, 0, len(nums)-1)
        self.radix_sort(nums)
        print(nums)
        max_margin = 0
        for i in range(len(nums)-1):
            margin = nums[i+1] - nums[i]
            if margin > max_margin:
                max_margin = margin
        return max_margin

    def quick_sort(self, nums, left, right):
        """
        in-place
        :param nums:
        :return:
        """
        if left >= right:
            return
        pivot = nums[left]
        low = left
        high = right
        while left < right:
            while left < right and nums[right] > pivot:
                right -= 1
            nums[left] = nums[right]
            while left<right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[right] = pivot
        self.quick_sort(nums, low, left-1)
        self.quick_sort(nums, left+1, high)

    def radix_sort(self, nums, radix=10):
        """
            基数排序
            先按低位进行排序(个位)，再按高位进行排序(十位)
            计算出需要几个维度(需要知道是什么进制)
            :param nums:
            :return:
            """
        import math
        # 注意100 bucket_num =2, 但是需要个、十、百三次排序
        bucket_num = int(math.ceil(math.log(max(nums), radix)))
        print("bucket_num:", bucket_num)
        for i in range(1, bucket_num+1+1):
            # i=1 表示第一轮个位 i=2 表示第2轮十位，以此类推
            # 获取要析取的数
            buckets = [[] for i in range(radix)]
            for val in nums:
                idx = int(val % (radix**i) / (radix ** (i-1)))
                buckets[idx].append(val)
            sorted_idx = 0
            for bucket in buckets:
                if bucket:
                    j = 0
                    while j < len(bucket):
                        nums[sorted_idx] = bucket[j]
                        sorted_idx += 1
                        j += 1


# nums = [3, 6, 9, 1]
nums = [1, 10000000]
# output 3
s = Solution()
print(s.maximumGap(nums))




