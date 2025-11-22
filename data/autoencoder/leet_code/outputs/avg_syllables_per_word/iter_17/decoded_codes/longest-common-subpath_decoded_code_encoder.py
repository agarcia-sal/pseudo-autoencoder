from typing import List, Set

class Solution:
    def longestCommonSubpath(self, number_of_cities: int, list_of_paths: List[List[int]]) -> int:
        def hash_subpaths(single_path: List[int], subpath_length: int) -> Set[int]:
            base_prime = 113
            modulus = 10**9 + 7
            hash_value = 0
            power = 1

            for i in range(subpath_length):
                hash_value = (hash_value * base_prime + single_path[i]) % modulus
                power = (power * base_prime) % modulus

            hashes = {hash_value}
            for i in range(subpath_length, len(single_path)):
                leading_element = single_path[i - subpath_length]
                trailing_element = single_path[i]
                hash_value = (hash_value * base_prime + trailing_element - leading_element * power) % modulus
                hashes.add(hash_value)
            return hashes

        def check_common_subpath(subpath_length: int) -> bool:
            if subpath_length == 0:
                return True
            common_hashes = hash_subpaths(list_of_paths[0], subpath_length)
            for path in list_of_paths[1:]:
                current_hashes = hash_subpaths(path, subpath_length)
                common_hashes &= current_hashes
                if not common_hashes:
                    return False
            return True

        left, right = 0, min(len(path) for path in list_of_paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check_common_subpath(mid):
                left = mid
            else:
                right = mid - 1
        return left