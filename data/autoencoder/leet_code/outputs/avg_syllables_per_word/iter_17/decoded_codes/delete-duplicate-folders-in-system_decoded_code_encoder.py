from collections import defaultdict
from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
        self.deleted: bool = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans: List[List[str]] = []
        root = TrieNode()
        subtreeToNodes: Dict[str, List[TrieNode]] = defaultdict(list)

        # Build the Trie from sorted paths
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        def buildSubtreeToRoots(node: TrieNode) -> str:
            # Build subtree serialization string including children's keys and their subtree serializations
            subtree = '(' + ''.join(
                s + buildSubtreeToRoots(node.children[s])
                for s in sorted(node.children.keys())
            ) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        # Mark nodes whose subtree serialization occurs more than once as deleted
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