from typing import List, Set

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # Helper function to compute all rolling hashes of subpaths of given length in a path
        def hash_subpaths(path: List[int], length: int) -> Set[int]:
            P = 113
            MOD = 10**9 + 7

            hash_value = 0
            power = 1
            for i in range(length):
                hash_value = (hash_value * P + path[i]) % MOD
                power = (power * P) % MOD

            hashes = {hash_value}
            for i in range(length, len(path)):
                # Remove the leftmost element and add the new rightmost element to rolling hash
                hash_value = (hash_value * P + path[i] - path[i - length] * power) % MOD
                # Python % operator always returns non-negative remainder
                hashes.add(hash_value)

            return hashes

        # Check if there exists a common subpath of given length among all paths
        def check_common_subpath(length: int) -> bool:
            if length == 0:
                return True

            common_hashes = hash_subpaths(paths[0], length)
            for path in paths[1:]:
                current_hashes = hash_subpaths(path, length)
                common_hashes &= current_hashes
                if not common_hashes:
                    return False
            return True

        left, right = 0, min(len(path) for path in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1

        return left