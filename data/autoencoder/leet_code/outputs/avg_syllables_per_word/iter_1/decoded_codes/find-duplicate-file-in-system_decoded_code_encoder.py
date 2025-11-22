from collections import defaultdict

def find_duplicate(paths):
    content_to_paths = defaultdict(list)
    for path in paths:
        dir, files_str = path.split(' ', 1)
        files = files_str.split()
        for f in files:
            name, content = f.split('(', 1)
            content = content[:-1]
            content_to_paths[content].append(dir + '/' + name)
    return [group for group in content_to_paths.values() if len(group) > 1]