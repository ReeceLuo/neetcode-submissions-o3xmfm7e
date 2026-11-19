class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isWord = True

    # if dot, must try every letter

    def dfs(self, node, word):
        curr = node
        for i, char in enumerate(word):
            if char == ".":
                for child in curr.children:
                    if child:
                        exists = self.dfs(child, word[i + 1:])
                        if exists:
                            return True
                return False
            else:
                index = ord(char) - ord('a')
                if not curr.children[index]:
                    return False
                curr = curr.children[index]
        return curr.isWord

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)






