from typing import List

class Solution:
    def maxProduct(self, list_of_numbers: List[int]) -> int:
        if not list_of_numbers:
            return 0

        maximum_product = minimum_product = result = list_of_numbers[0]

        for number in list_of_numbers[1:]:
            if number < 0:
                maximum_product, minimum_product = minimum_product, maximum_product

            maximum_product = max(number, maximum_product * number)
            minimum_product = min(number, minimum_product * number)
            result = max(result, maximum_product)

        return result