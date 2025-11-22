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

        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node: TrieNode) -> str:
            # Build serialized subtree string using parentheses to denote structure
            subtree = "("
            for s in node.children:
                subtree += s + buildSubtreeToRoots(node.children[s])
            subtree += ")"
            if subtree != "()":
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