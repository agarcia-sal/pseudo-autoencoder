from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                idx = file_info.find('(')
                file_name = file_info[:idx]
                content = file_info[idx+1:-1]
                content_to_paths[content].append(directory + '/' + file_name)
        return [group for group in content_to_paths.values() if len(group) > 1]