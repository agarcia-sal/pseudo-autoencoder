from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                open_idx = file_info.find('(')
                file_name = file_info[:open_idx]
                content = file_info[open_idx+1:-1]  # exclude the closing parenthesis
                content_to_paths[content].append(f"{directory}/{file_name}")
        result = []
        for group_of_paths in content_to_paths.values():
            if len(group_of_paths) > 1:
                result.append(group_of_paths)
        return result