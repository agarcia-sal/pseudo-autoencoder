from collections import defaultdict
from typing import List, Dict, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
        self.deleted: bool = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans: List[List[str]] = []
        root = TrieNode()
        subtreeToNodes: Dict[str, List[TrieNode]] = defaultdict(list)

        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node: TrieNode) -> str:
            # subtree serialization: "(" + concatenation of each child's name + child's subtree + ")"
            # children sorted by key to maintain consistent ordering
            subtree = '('
            for s in sorted(node.children):
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