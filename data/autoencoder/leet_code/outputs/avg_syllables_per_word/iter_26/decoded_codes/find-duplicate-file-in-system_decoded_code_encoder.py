from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                open_paren_idx = file_info.find('(')
                close_paren_idx = file_info.rfind(')')
                file_name = file_info[:open_paren_idx]
                content = file_info[open_paren_idx + 1:close_paren_idx]

                content_to_paths[content].append(f"{directory}/{file_name}")

        result = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return result