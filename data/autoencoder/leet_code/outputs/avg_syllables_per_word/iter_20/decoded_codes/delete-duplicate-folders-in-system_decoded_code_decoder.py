from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans = []
        root = TrieNode()
        subtreeToNodes = defaultdict(list)

        # Insert all paths into trie
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node: TrieNode) -> str:
            # Compute subtree serialization in lex order of keys for determinism
            # Format: '(' + concat of (child_name + child_subtree) + ')'
            subtree = '('
            for s in sorted(node.children.keys()):
                subtree += s + buildSubtreeToRoots(node.children[s])
            subtree += ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        def constructPath(node: TrieNode, path: List[str]) -> None:
            for s, child in node.children.items():
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])

        return ans