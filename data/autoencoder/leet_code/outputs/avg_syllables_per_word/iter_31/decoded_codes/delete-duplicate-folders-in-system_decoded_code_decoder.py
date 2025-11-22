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

        # Insert each path into the Trie
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node):
            # Build the serialization of the subtree rooted at this node
            subtree = '('
            for s in sorted(node.children):
                subtree += s + buildSubtreeToRoots(node.children[s])
            subtree += ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        # Mark duplicate subtrees as deleted
        for nodes_list in subtreeToNodes.values():
            if len(nodes_list) > 1:
                for node in nodes_list:
                    node.deleted = True

        def constructPath(node, path):
            for s, child in node.children.items():
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])
        return ans