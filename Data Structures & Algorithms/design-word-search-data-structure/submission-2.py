class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.isWord = True

    # when there is ".", we need to try every letter and dfs
    # if dfs exists, return true. if not, continue

    def dfs(self, node, word):
        curr = node
        for i, char in enumerate(word):
            if char == ".": # try every letter
                for child in curr.children:
                    if child is not None:
                        exists = self.dfs(child, word[i + 1:])
                        if exists:
                            return True
                return False
            else:
                index = ord(char) - ord("a")
                if curr.children[index] is None:
                    return False
                curr = curr.children[index]
        return curr.isWord

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
