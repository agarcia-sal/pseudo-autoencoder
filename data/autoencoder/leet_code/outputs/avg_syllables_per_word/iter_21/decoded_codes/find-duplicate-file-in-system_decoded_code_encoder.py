from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            directory = parts[0]

            for file_info in parts[1:]:
                file_name_and_content = file_info.split('(')
                file_name = file_name_and_content[0]
                content_with_closing = file_name_and_content[1]
                content = content_with_closing[:-1]

                content_to_paths[content].append(directory + '/' + file_name)

        result = []
        for paths_group in content_to_paths.values():
            if len(paths_group) > 1:
                result.append(paths_group)

        return result