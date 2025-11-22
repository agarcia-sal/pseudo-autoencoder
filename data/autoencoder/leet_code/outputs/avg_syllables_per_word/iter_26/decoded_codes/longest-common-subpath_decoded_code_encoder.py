class Solution:
    def longestCommonSubpath(self, number_of_cities, list_of_paths):
        def hash_subpaths(path, length):
            base_prime = 113
            modulus = 10**9 + 7
            hash_value = 0
            power = 1

            # Compute the hash for the first 'length' elements
            for i in range(length):
                hash_value = (hash_value * base_prime + path[i]) % modulus
                power = (power * base_prime) % modulus

            hashes = {hash_value}

            # Rolling hash computation for subsequent subpaths of 'length'
            for i in range(length, len(path)):
                hash_value = (hash_value * base_prime + path[i] - path[i - length] * power) % modulus
                hashes.add(hash_value)

            return hashes

        def check_common_subpath(length):
            if length == 0:
                return True

            common_hashes = hash_subpaths(list_of_paths[0], length)
            for path in list_of_paths[1:]:
                current_hashes = hash_subpaths(path, length)
                common_hashes &= current_hashes
                if not common_hashes:
                    return False
            return True if common_hashes else False

        left = 0
        right = min(len(path) for path in list_of_paths)

        while left < right:
            middle = (left + right + 1) // 2
            if check_common_subpath(middle):
                left = middle
            else:
                right = right - 1

        return left