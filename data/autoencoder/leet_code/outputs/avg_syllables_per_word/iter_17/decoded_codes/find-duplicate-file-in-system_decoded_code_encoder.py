from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                file_name = file_info[:file_info.index('(')]
                content = file_info[file_info.index('(') + 1:-1]
                content_to_paths[content].append(directory + '/' + file_name)
        return [paths for paths in content_to_paths.values() if len(paths) > 1]