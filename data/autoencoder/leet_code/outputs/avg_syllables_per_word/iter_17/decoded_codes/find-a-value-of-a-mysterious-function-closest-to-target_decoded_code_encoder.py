class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')
        for number in arr:
            temp_set = {number & element for element in seen}
            temp_set.add(number)
            seen = temp_set
            for value in seen:
                current_difference = abs(value - target)
                if current_difference < min_diff:
                    min_diff = current_difference
        return min_diff