# 621 任务调度器 https://leetcode-cn.com/problems/task-scheduler/

# 计算完成任务需要的最短时间

from collections import defaultdict
from collections import OrderedDict


class Solution:
    def leastInterval(self, tasks, n):
        """
        1. 先数量最多的元素
        # 待命: "wait"
        :param tasks:
        :param n:
        :return:
        """
        res = []
        task_dict =  defaultdict(int)
        for task in tasks:
            task_dict[task] += 1
        task_dict = OrderedDict(sorted(task_dict.items(), key=lambda x: x[-1], reverse=True))
        print(task_dict)
        for k, v in task_dict.items():
            if not res:
                item = [k] + [""]*n
                res.extend(item * v)
            print("res:", res)
            if k in res:
                continue
            idx = self.is_full(res)
            print("idx:", idx)
            # 表示未满
            if idx >= 0 and k not in res:
                while v and idx < len(res):
                    res[idx] = k
                    idx = idx + n + 1
                    v -= 1
                print("res:", res)
                if v >0:
                    print("v:{}, idx:{}".format(v, idx))
                    print("len(res):", len(res))
                    # 超出边界的元素朝后加，继续增加数组长度
                    res.extend([""]*(idx - len(res)))
                    print("res:", res)
                    item = [k] + [""]*n
                    res.extend(item*v)
                    print("res:", res)
        time = self.last_idx(res) + 1
        return time

    def is_full(self, res):
        """
        判断list是否满，没有空字符串认为是满
        :param res:
        :return:
        """
        for i, item in enumerate(res):
            if not item:
                return i
        # 当res满时，需要继续扩充元素
        return len(res)

    def last_idx(self, res):
        """
        找到最后一个字符的索引
        :param res:
        :return:
        """
        last_idx = 0
        for i, item in enumerate(res):
            if item:
                last_idx = i
        return last_idx


tasks = ["A", "A", "B", "B", "B", "A"]
tasks = ["A", "A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D", "E", "E"]
# tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
s= Solution()
print(s.leastInterval(tasks, n))

####

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1

        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length













