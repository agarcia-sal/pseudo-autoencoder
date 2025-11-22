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

        for path in sorted(paths):
            node = root
            for folder_name in path:
                node = node.children[folder_name]

        def buildSubtreeToRoots(node):
            # Build a string representation of the subtree, sorted by child names
            subtree = '(' + ''.join(
                child_name + buildSubtreeToRoots(child_node)
                for child_name, child_node in sorted(node.children.items())
            ) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        for nodes_list in subtreeToNodes.values():
            if len(nodes_list) > 1:
                for node_element in nodes_list:
                    node_element.deleted = True

        def constructPath(node, path):
            for child_name, child_node in node.children.items():
                if not child_node.deleted:
                    constructPath(child_node, path + [child_name])
            if path:
                ans.append(path)

        constructPath(root, [])
        return ans