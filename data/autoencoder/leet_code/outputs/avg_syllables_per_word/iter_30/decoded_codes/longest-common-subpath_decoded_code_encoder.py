class Solution:
    def longestCommonSubpath(self, n, paths):
        def hash_subpaths(path, length):
            base = 113
            modulus = 10**9 + 7
            hash_value = 0
            power = 1
            for i in range(length):
                hash_value = (hash_value * base + path[i]) % modulus
                power = (power * base) % modulus
            hashes = {hash_value}
            for i in range(length, len(path)):
                hash_value = (hash_value * base + path[i] - path[i - length] * power) % modulus
                hashes.add(hash_value)
            return hashes

        def check_common_subpath(length):
            if length == 0:
                return True
            common_hashes = hash_subpaths(paths[0], length)
            for path in paths[1:]:
                current_hashes = hash_subpaths(path, length)
                common_hashes &= current_hashes
                if not common_hashes:
                    return False
            return bool(common_hashes)

        left, right = 0, min(len(path) for path in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1
        return left