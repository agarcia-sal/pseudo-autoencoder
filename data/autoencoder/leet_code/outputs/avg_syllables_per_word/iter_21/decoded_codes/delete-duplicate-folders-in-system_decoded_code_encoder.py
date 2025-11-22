from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        ans = []
        root = TrieNode()
        subtreeToNodes = defaultdict(list)

        # Build the trie
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node):
            # Construct the subtree string representation
            subtree = '('
            for s in sorted(node.children):
                subtree += s + buildSubtreeToRoots(node.children[s])
            subtree += ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        # Mark duplicate subtrees as deleted
        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        def constructPath(node, path):
            for s in sorted(node.children):
                child = node.children[s]
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])
        return ans