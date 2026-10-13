class PrefixTree:

    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True








        