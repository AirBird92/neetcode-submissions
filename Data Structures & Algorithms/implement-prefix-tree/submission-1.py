class TreeNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self.offset = ord('a')

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - self.offset
            if not cur.children[idx]:
                cur.children[idx] = TreeNode()
            cur = cur.children[idx]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - self.offset
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - self.offset
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True