class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self, bit_len=15):
        self.root = TrieNode()
        self.bit_len = bit_len

    def insert(self, num):
        node = self.root
        for i in range(self.bit_len, -1, -1):
            b = (num >> i) & 1
            if b not in node.children:
                node.children[b] = TrieNode()
            node = node.children[b]
            node.count += 1

    def count_less_than(self, num, threshold):
        c = 0
        node = self.root
        for i in range(self.bit_len, -1, -1):
            if node is None:
                break
            b = (num >> i) & 1
            tb = (threshold >> i) & 1
            if tb == 1:
                c += node.children.get(b, TrieNode()).count
                node = node.children.get(b ^ 1)
            else:
                node = node.children.get(b)
        return c

def countPairs(nums, low, high):
    trie = Trie()
    pairs = 0
    for n in nums:
        pairs += trie.count_less_than(n, high + 1) - trie.count_less_than(n, low)
        trie.insert(n)
    return pairs