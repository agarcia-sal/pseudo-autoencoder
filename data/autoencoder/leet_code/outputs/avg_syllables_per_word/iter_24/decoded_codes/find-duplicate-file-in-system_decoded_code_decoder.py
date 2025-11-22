from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                # file_info format: filename(content)
                # Find first '('
                open_paren_idx = file_info.find('(')
                file_name = file_info[:open_paren_idx]
                content = file_info[open_paren_idx+1:-1]  # exclude trailing ')'
                content_to_paths[content].append(directory + '/' + file_name)
        result = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return result