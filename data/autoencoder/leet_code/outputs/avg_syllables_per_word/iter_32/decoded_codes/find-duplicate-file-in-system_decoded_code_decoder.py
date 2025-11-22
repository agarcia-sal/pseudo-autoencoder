from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                # Find the first '(' to split file name and content
                idx = file_info.find('(')
                if idx == -1 or not file_info.endswith(')'):
                    # Invalid format, skip this file_info robustly
                    continue
                file_name = file_info[:idx]
                content = file_info[idx+1:-1]
                content_to_paths[content].append(directory + '/' + file_name)
        result = [paths_list for paths_list in content_to_paths.values() if len(paths_list) > 1]
        return result