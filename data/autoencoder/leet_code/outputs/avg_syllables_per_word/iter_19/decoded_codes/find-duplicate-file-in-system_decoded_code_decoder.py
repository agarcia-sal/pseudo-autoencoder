from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            directory = parts[0]

            for file_info in parts[1:]:
                open_paren_pos = file_info.find('(')
                file_name = file_info[:open_paren_pos]
                content = file_info[open_paren_pos + 1:-1]
                content_to_paths[content].append(directory + '/' + file_name)

        result = [paths_group for paths_group in content_to_paths.values() if len(paths_group) > 1]
        return result