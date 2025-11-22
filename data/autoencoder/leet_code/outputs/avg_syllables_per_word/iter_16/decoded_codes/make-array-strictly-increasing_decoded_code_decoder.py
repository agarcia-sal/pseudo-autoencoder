from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        dp = {-1: 0}  # key: last number used, value: min operations to get here

        for number in arr1:
            new_dp = {}
            for last_number, operations in dp.items():
                if number > last_number:
                    if number in new_dp:
                        new_dp[number] = min(new_dp[number], operations)
                    else:
                        new_dp[number] = operations

                index = bisect_right(arr2, last_number)
                if index < len(arr2):
                    replacement_number = arr2[index]
                    if replacement_number in new_dp:
                        new_dp[replacement_number] = min(new_dp[replacement_number], operations + 1)
                    else:
                        new_dp[replacement_number] = operations + 1

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())