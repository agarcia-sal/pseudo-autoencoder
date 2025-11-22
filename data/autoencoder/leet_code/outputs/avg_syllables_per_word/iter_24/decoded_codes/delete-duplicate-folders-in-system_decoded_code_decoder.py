from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: defaultdict[str, TrieNode] = defaultdict(TrieNode)
        self.deleted: bool = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans: List[List[str]] = []
        root = TrieNode()
        subtreeToNodes: defaultdict[str, List[TrieNode]] = defaultdict(list)

        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node: TrieNode) -> str:
            # Serialize each subtree rooted at node as "(s<child_subtree>...)" sorted by children names
            parts = []
            for s in sorted(node.children):
                parts.append(s + buildSubtreeToRoots(node.children[s]))
            subtree = "(" + "".join(parts) + ")"
            if subtree != "()":
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        def constructPath(node: TrieNode, path: List[str]) -> None:
            for s, child in sorted(node.children.items()):
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])

        return ans