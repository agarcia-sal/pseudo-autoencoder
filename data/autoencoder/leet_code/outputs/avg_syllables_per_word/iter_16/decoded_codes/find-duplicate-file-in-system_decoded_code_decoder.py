from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                content_to_paths[content].append(f"{directory}/{file_name}")
        return [paths for paths in content_to_paths.values() if len(paths) > 1]