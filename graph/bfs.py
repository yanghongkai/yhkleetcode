
# 广度优先搜索用于解决最短路径问题

# 1. 创建一个队列，用于存储要检查的人
# 2. 从队列中弹出一个人
# 3. 检查这个人是否是芒果经销商
# 4.a. 是，大功告成 4.b. 否,将这个人的所有邻居都加入队列
# 5. 回到第二步
# 6. 如果队列为空，就说明你的人机关系网中没有芒果经销商


from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 这个数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")








