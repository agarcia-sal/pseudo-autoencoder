from collections import defaultdict
from typing import List, Dict


class TrieNode:
    def __init__(self):
        # Each missing key creates a new TrieNode (using defaultdict with a factory)
        self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
        self.deleted: bool = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans: List[List[str]] = []
        root = TrieNode()
        subtreeToNodes: Dict[str, List[TrieNode]] = defaultdict(list)

        # Build Trie from sorted paths
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children[s]

        # Helper function to serialize subtrees and group nodes with identical subtree
        def buildSubtreeToRoots(node: TrieNode) -> str:
            # Natural order of keys: lex sorted order
            subtree_parts = []
            for s in sorted(node.children.keys()):
                child_subtree = buildSubtreeToRoots(node.children[s])
                subtree_parts.append(s + child_subtree)
            subtree = '(' + ''.join(subtree_parts) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        # Mark all nodes that belong to duplicate subtrees as deleted
        for nodes_list in subtreeToNodes.values():
            if len(nodes_list) > 1:
                for node in nodes_list:
                    node.deleted = True

        # Reconstruct the answer paths from non-deleted nodes
        def constructPath(node: TrieNode, path: List[str]) -> None:
            for s, child_node in node.children.items():
                if not child_node.deleted:
                    constructPath(child_node, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])

        return ans