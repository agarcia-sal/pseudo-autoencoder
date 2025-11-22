class Solution:
    def findDuplicate(self, paths):
        content_to_paths = {}
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(', 1)
                content = content[:-1]
                if content not in content_to_paths:
                    content_to_paths[content] = []
                content_to_paths[content].append(directory + "/" + file_name)
        result = []
        for path_list in content_to_paths.values():
            if len(path_list) > 1:
                result.append(path_list)
        return result