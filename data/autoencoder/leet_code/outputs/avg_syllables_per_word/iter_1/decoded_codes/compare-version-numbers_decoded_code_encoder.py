def compare_versions(v1, v2):
    v1_parts = v1.split('.')
    v2_parts = v2.split('.')
    max_len = max(len(v1_parts), len(v2_parts))
    for i in range(max_len):
        x = int(v1_parts[i]) if i < len(v1_parts) else 0
        y = int(v2_parts[i]) if i < len(v2_parts) else 0
        if x < y:
            return -1
        if x > y:
            return 1
    return 0