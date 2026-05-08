# Last updated: 5/7/2026, 5:18:24 PM
class PrefixTree:
    class Node:
        def __init__(self):
            self.children = collections.defaultdict(PrefixTree.Node)
            self.terminal = False

    def __init__(self):
        self.root = self.Node()

    def add(self, w):
        current = self.root

        for c in w:
            current = current.children[c]

        current.terminal = True

    def contains(self, w):
        def iterate(node, subw):
            if subw == "":
                return node.terminal

            if subw[0] == ".":
                results = [iterate(child, subw[1:]) for child in node.children.values()]
                return any(results)

            if subw[0] in node.children:
                return iterate(node.children[subw[0]], subw[1:])

            return False

        return iterate(self.root, w)

class WordDictionary:

    def __init__(self):
        self.tree = PrefixTree()
        self.cache = {}
        

    def addWord(self, word: str) -> None:
        self.cache = {}
        self.tree.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.cache:
            return self.cache[word]

        result = self.tree.contains(word)
        self.cache[word] = result
        return result
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)