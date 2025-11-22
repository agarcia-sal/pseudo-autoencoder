class Solution:
    def longestCommonSubpath(self, n, paths):
        P = 113
        MOD = 10**9 + 7

        def hash_subpaths(path, length):
            if length == 0:
                return set()
            hash_value = 0
            power = 1
            for i in range(length):
                hash_value = (hash_value * P + path[i]) % MOD
                power = (power * P) % MOD
            hashes = {hash_value}
            for i in range(length, len(path)):
                hash_value = ((hash_value * P + path[i]) - path[i - length] * power) % MOD
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

        left, right = 0, min(len(p) for p in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1
        return left