class Solution:
    def maxDistance(self, arrays):
        minimum_value = arrays[0][0]
        maximum_value = arrays[0][-1]
        maximum_distance = 0

        for index in range(1, len(arrays)):
            current_array = arrays[index]
            current_minimum = current_array[0]
            current_maximum = current_array[-1]

            maximum_distance = max(
                maximum_distance,
                abs(current_maximum - minimum_value),
                abs(maximum_value - current_minimum)
            )

            minimum_value = min(minimum_value, current_minimum)
            maximum_value = max(maximum_value, current_maximum)

        return maximum_distance