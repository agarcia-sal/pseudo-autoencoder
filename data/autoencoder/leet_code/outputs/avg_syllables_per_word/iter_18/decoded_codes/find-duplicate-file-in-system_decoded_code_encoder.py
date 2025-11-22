from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                left_paren_idx = file_info.find('(')
                file_name = file_info[:left_paren_idx]
                content = file_info[left_paren_idx + 1:-1]
                content_to_paths[content].append(directory + '/' + file_name)
        result = []
        for paths_group in content_to_paths.values():
            if len(paths_group) > 1:
                result.append(paths_group)
        return result