class Solution:
    def findDuplicate(self, paths):
        content_to_paths = {}
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content_with_paren = file_info.split("(")
                content = content_with_paren[:-1]
                content_to_paths.setdefault(content, []).append(f"{directory}/{file_name}")
        return [paths for paths in content_to_paths.values() if len(paths) > 1]