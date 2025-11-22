from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                file_name = file_info[:file_info.index('(')]
                content_key = file_info[file_info.index('(') + 1 : file_info.index(')')]
                content[content_key].append(f"{directory}/{file_name}")
        result = [group for group in content.values() if len(group) > 1]
        return result