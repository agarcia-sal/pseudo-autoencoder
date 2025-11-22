from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def insert(root, value):
    cur = root
    for i in range(17, -1, -1):
        bit = (value >> i) & 1
        if bit not in cur.children:
            cur.children[bit] = TrieNode()
        cur = cur.children[bit]
        cur.count += 1

def erase(root, value):
    cur = root
    for i in range(17, -1, -1):
        bit = (value >> i) & 1
        cur = cur.children[bit]
        cur.count -= 1

def max_xor(root, value):
    cur = root
    res = 0
    for i in range(17, -1, -1):
        bit = (value >> i) & 1
        flip = 1 - bit
        if flip in cur.children and cur.children[flip].count > 0:
            res |= (1 << i)
            cur = cur.children[flip]
        else:
            cur = cur.children.get(bit)
            if cur is None:
                break
    return res

def solve(parents, queries):
    # Build tree from parents list
    n = len(parents)
    tree = defaultdict(list)
    root = -1
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            tree[p].append(i)

    # Group queries by node
    node_queries = defaultdict(list)
    for i, (node, val) in enumerate(queries):
        node_queries[node].append(val)

    # Map queries to index
    query_idx = {}
    for i, (node, val) in enumerate(queries):
        query_idx[(node, val)] = i

    result = [0] * len(queries)
    trie_root = TrieNode()

    def dfs(node):
        insert(trie_root, node)
        for val in node_queries[node]:
            result[query_idx[(node, val)]] = max_xor(trie_root, val)
        for child in tree[node]:
            dfs(child)
        erase(trie_root, node)

    dfs(root)
    return result