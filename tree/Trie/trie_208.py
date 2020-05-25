
# 208实现Trie(前缀树) https://leetcode-cn.com/problems/implement-trie-prefix-tree/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china


class Trie:
    """
    用嵌套dict实现
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            # 如果存在key，再继续沿着路径迭代
            # 如果不存在key,则在当前路径中创建key,考虑上述两个情况，可以使用setdefault()
            current = current.setdefault(char, {})  # 等同于get()
        current.setdefault("_end")

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if char in current:
                current = current[char]
            # 如果key不存在，则返回False
            else:
                return False
        if "_end" in current:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char in current:
                current = current[char]
            else:
                return False
        return True


