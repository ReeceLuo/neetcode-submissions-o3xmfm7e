# allow for adding words and searching for them
# dots can be matched to any letter
    # need to find a way to conitnue when reaching dot
    # search all children and try exploring?

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
    
    def dfs(self, node, word):
        curr = node
        for i, char in enumerate(word):
            if char == ".":
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



