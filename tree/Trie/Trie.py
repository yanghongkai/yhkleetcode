
# Trie | (Insert and Search) https://www.geeksforgeeks.org/trie-insert-and-search/


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord("a")

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node, just marks leaf node
        pcrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            # if current character is not present
            if not pcrawl.children[index]:
                pcrawl.children[index] = self.get_node()
            pcrawl = pcrawl.children[index]

        # mark last node as leaf
        pcrawl.is_end_of_word = True

    def search(self, key):
        """
        2_search key in the trie
        returns true if key presents in trie, else false
        :param key:
        :return:
        """
        pcrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not pcrawl.children[index]:
                return False
            pcrawl = pcrawl.children[index]

        return pcrawl!=None and pcrawl.is_end_of_word


def main():
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]














