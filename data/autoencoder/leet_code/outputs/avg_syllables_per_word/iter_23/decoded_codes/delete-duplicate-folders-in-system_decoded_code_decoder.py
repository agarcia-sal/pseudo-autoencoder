from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.deleted = False


class Solution:
    def deleteDuplicateFolder(self, paths):
        ans = []
        root = TrieNode()
        subtreeToNodes = defaultdict(list)

        # Build the Trie with sorted paths
        for path in sorted(paths):
            node = root
            for folder_name in path:
                if folder_name not in node.children:
                    node.children[folder_name] = TrieNode()
                node = node.children[folder_name]

        def buildSubtreeToRoots(node):
            # Build encoded subtree string
            # Encoding: "(" + for each (folder_name + subtree of child) + ")"
            parts = []
            for folder_name in sorted(node.children):
                child = node.children[folder_name]
                parts.append(folder_name + buildSubtreeToRoots(child))
            subtree = "(" + "".join(parts) + ")"
            if subtree != "()":
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        for nodes_list in subtreeToNodes.values():
            if len(nodes_list) > 1:
                for node in nodes_list:
                    node.deleted = True

        def constructPath(node, path):
            for folder_name, child_node in node.children.items():
                if not child_node.deleted:
                    constructPath(child_node, path + [folder_name])
            if len(path) > 0:
                ans.append(path)

        constructPath(root, [])
        return ans