
# 146 LRU缓存机制  https://leetcode-cn.com/problems/lru-cache/solution/lru-huan-cun-ji-zhi-by-leetcode/

from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """

        Args:
            capacity:
        """
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


cache = LRUCache(2)
cache.put(1, 1)
print(cache)
cache.put(2, 2)
print(cache)
cache.get(1)
print(cache)
cache.put(3, 3)
print(cache)
print(cache.get(2))
cache.put(4, 4)
print(cache)
cache.get(3)
print(cache)
cache.get(4)
print(cache)










