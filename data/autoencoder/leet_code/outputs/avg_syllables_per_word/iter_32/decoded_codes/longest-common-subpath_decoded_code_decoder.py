from typing import List, Set

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        base = 113
        modulus = 10**9 + 7

        def hash_subpaths(path: List[int], length: int) -> Set[int]:
            if length == 0:
                return set()
            hash_value = 0
            power = 1
            # Compute hash of first 'length' elements and power = base^length % modulus
            for i in range(length):
                hash_value = (hash_value * base + path[i]) % modulus
                power = (power * base) % modulus
            hashes = {hash_value}
            # Rolling hash for subsequent subpaths
            for i in range(length, len(path)):
                # Remove contribution of path[i - length]*power and add new element path[i]
                hash_value = (hash_value * base - path[i - length] * power + path[i]) % modulus
                # Python's modulo can yield negative, ensure non-negative
                if hash_value < 0:
                    hash_value += modulus
                hashes.add(hash_value)
            return hashes

        def check_common_subpath(length: int) -> bool:
            if length == 0:
                return True
            common_hashes = hash_subpaths(paths[0], length)
            if not common_hashes:
                return False
            for path in paths[1:]:
                current_hashes = hash_subpaths(path, length)
                common_hashes = common_hashes & current_hashes
                if not common_hashes:
                    return False
            return len(common_hashes) > 0

        left, right = 0, min(len(path) for path in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1
        return left