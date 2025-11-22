from typing import List, Set

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def hash_subpaths(path: List[int], length: int) -> Set[int]:
            base_number = 113
            modulus = 10**9 + 7
            hash_value = 0
            power = 1

            # Compute hash of the first 'length' elements and power = base_number^length % modulus
            for i in range(length):
                hash_value = (hash_value * base_number + path[i]) % modulus
                power = (power * base_number) % modulus

            hashes = {hash_value}

            for i in range(length, len(path)):
                # Rolling hash: remove leftmost element, add new rightmost element
                hash_value = (hash_value * base_number - path[i - length] * power + path[i]) % modulus
                # Correct possible negative modulo result
                hashes.add(hash_value)

            return hashes

        def check_common_subpath(length: int) -> bool:
            if length == 0:
                return True
            common_hashes = hash_subpaths(paths[0], length)
            for path in paths[1:]:
                current_hashes = hash_subpaths(path, length)
                common_hashes = common_hashes.intersection(current_hashes)
                if not common_hashes:
                    return False
            return True

        left, right = 0, min(len(p) for p in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1
        return left