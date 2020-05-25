
# Implementing a Trie in Python (in less than 100 lines of code) https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1


class Trie(object):
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        """
        逐字符插入
        Args:
            word:

        Returns:

        """
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                # if char exists
                if char == child.char:
                    node = child
                    found_in_child = True
                    node.counter += 1
                    break

            # char not exists
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # 从插入的节点开始查找
                node = new_node
        node.word_finished = True

    def find_prefix(self, prefix):
        """
        找到返回(True, count),未找到返回(False, 0)
        Args:
            prefix:

        Returns:

        """
        node = self.root
        if not node.children:
            return False, 0
        for char in prefix:
            char_is_exist = False
            for child in node.children:
                if char == child.char:
                    node = child
                    char_is_exist = True
                    break

            if not char_is_exist:
                return False, 0

        return True, node.counter


trie = Trie()
trie.add("hackathon")
trie.add("hack")

print(trie.find_prefix("hac"))
print(trie.find_prefix("hack"))
print(trie.find_prefix("hackathon"))
print(trie.find_prefix("ha"))
print(trie.find_prefix("hammer"))



