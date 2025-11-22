from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(', 1)
                content = content[:-1]  # remove trailing ')'
                content_to_paths[content].append(f"{directory}/{file_name}")
        result = [group for group in content_to_paths.values() if len(group) > 1]
        return result