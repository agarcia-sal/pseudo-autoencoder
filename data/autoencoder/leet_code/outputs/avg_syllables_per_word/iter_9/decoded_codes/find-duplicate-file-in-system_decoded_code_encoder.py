class Solution:
    def findDuplicate(self, paths):
        content_to_paths = {}
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                content_to_paths.setdefault(content, []).append(directory + '/' + file_name)
        return [group for group in content_to_paths.values() if len(group) > 1]