

class ListNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    """
    head->next 存储最久不访问的
    tail->prev 存储最近访问的
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap= {}
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        """
        将元素移动到尾部
        Args:
            key:

        Returns:

        """
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def get(self, key):
        if key in self.hashmap:
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key, value):
        # 最新操作的都放到tail
        # when key in self.hashmap, update value
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            # when key not in self.hashmap and capacity full, 删掉hashmap中的值, 删除head->next
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next  # next这条链已经断掉
                self.head.next.prev = self.head

            # when key not in self.hashmap, 移动到tail
            # 插入新元素都要执行
            # insert element, 将其插入到tail
            new = ListNode(key, value)
            self.hashmap[key] = new
            self.tail.prev.next = new
            new.next = self.tail
            new.prev = self.tail.prev
            self.tail.prev = new

    def __str__(self):
        s_l = []
        p = self.head.next
        while p and p != self.tail:
            s_l.append("({}-{})".format(p.key, p.value))

            p = p.next
        # print("keys:", list(self.hashmap.keys()))
        return " ".join(s_l)


cache = LRUCache(2)

cache.put(1, 1)
print(cache)
cache.put(2, 2)
print(cache)
cache.get(1)
print(cache)
cache.put(3, 3)
print(cache)
cache.get(2)
print(cache)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)

print(cache)








