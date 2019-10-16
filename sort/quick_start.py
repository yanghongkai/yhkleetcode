
# 十大排序算法 sort algorithm https://www.jianshu.com/p/a1e97094f61b

# 快排
# 基线条件: len(arr)<2: return arr
# 问题分解: 所有小于pivot的数组，pivot, 所有大于pivot的数组


def quick_sort_1(arr):
    """
    O(nlogn)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    # 基准值
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort_1(less) + [pivot] + quick_sort_1(greater)


def select_sort_1(arr):
    """
    O(n^2)
    每次从剩余无序数组中选取一个最小的
    :param arr:
    :return:
    """
    res = []
    for i in range(len(arr)):
        idx = find_smallest(arr)
        item = arr.pop(idx)
        res.append(item)
    return res


def find_smallest(arr):
    """
    找出候选数组中最小的元素
    :param arr:
    :return:
    """
    small = arr[0]
    small_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_idx = i
    return small_idx


# =======================================================

# 快速排序
def quick_sort(arr, left, right):
    """
    in-place
    O(n)
    双指针最快
    :param arr:
    :return:
    """
    print("{}->{}:".format(left, right))
    if left >= right:
        return
    low = left
    high = right
    pivot = arr[left]
    while left < right:
        # 从右侧找到第一个<pivot的数
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]
        # 从左侧找到第一个>pivot的数
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[right] = pivot
    quick_sort(arr, low, left-1)
    quick_sort(arr, left+1, high)


# 选择排序
def select_sort(arr):
    """
    in-place
    :param arr:
    :return:
    """
    # 只需要进行n-1次选择即可
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 直接插入排序
def insert_sort(arr):
    """
    将未排序的元素直接插入到已排序的元素中，插入过程是从后向前找，直到找到第一个比它小的元素，插入进去
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        cur_v = arr[i]
        while arr[i-1] > cur_v and i>=1:
            arr[i] = arr[i-1]
            i = i-1
        arr[i] = cur_v
    return arr


# 冒泡排序
def bubble_sort(arr):
    """
    in-place
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# 归并排序
# 1. 申请空间，存放合并后的序列
# 2. 设定2个指针，最初位置分别为两个已经排序序列的起始位置
# 3. 比较两个指针所指向的元素，选择相对较小的元素放入到合并空间，并移动指针到下一位置
# 重复3， 直到某一指针超出序列尾
# 4. 将另一序列生肖的所有元素直接复制到合并序列尾部


def merge_sort(arr):
    """
    分解: 从上往下
    合并: 从小往上
    O(n)
    :param arr:
    :return:
    """
    import math
    if len(arr) < 2:
        return arr
    mid = math.floor(len(arr)/2)
    left, right = arr[0:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(arr1, arr2):
    """

    :param arr1:
    :param arr2:
    :return:
    """
    left = 0
    right = 0
    res = []

    while left<len(arr1) and right<len(arr2):
        if arr1[left] <= arr2[right]:
            res.append(arr1[left])
            left += 1
        else:
            res.append(arr2[right])
            right += 1
    # arr1 先超出序列尾
    if left == len(arr1):
        res.extend(arr2[right:])
    if right == len(arr2):
        res.extend(arr1[left:])
    return res




arr = [3, 5, 2, 1, 4]
# quick_sort(arr, 0, len(arr)-1)
# select_sort(arr)

# print(arr)
# print(bubble_sort(arr))
# print(insert_sort(arr))
print(merge_sort(arr))


