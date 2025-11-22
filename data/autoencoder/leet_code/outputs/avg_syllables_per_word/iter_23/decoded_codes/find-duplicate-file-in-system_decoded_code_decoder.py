from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                open_paren_index = file_info.find('(')
                file_name = file_info[:open_paren_index]
                content = file_info[open_paren_index+1:-1]  # from after '(' to before ')'
                content_to_paths[content].append(directory + '/' + file_name)

        result = [paths_group for paths_group in content_to_paths.values() if len(paths_group) > 1]
        return result