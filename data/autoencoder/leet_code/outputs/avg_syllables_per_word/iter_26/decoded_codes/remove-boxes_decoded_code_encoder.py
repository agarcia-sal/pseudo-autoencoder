class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        def dp(left_index: int, right_index: int, carry_count: int, memoization_map: dict) -> int:
            if left_index > right_index:
                return 0

            key = (left_index, right_index, carry_count)
            if key in memoization_map:
                return memoization_map[key]

            # Optimize by grouping boxes of the same color at the end
            while right_index > left_index and boxes[right_index] == boxes[right_index - 1]:
                right_index -= 1
                carry_count += 1

            result = dp(left_index, right_index - 1, 0, memoization_map) + (carry_count + 1) ** 2

            for i in range(left_index, right_index):
                if boxes[i] == boxes[right_index]:
                    candidate = dp(left_index, i, carry_count + 1, memoization_map) + dp(i + 1, right_index - 1, 0, memoization_map)
                    if candidate > result:
                        result = candidate

            memoization_map[key] = result
            return result

        return dp(0, len(boxes) - 1, 0, {})