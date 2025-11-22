class Solution:
    def minInteger(self, num: str, k: int) -> str:
        arr = list(num)
        n = len(arr)

        while k > 0:
            swap_occurred = False
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    smallest_char = '9'
                    pos_of_smallest = -1
                    limit = min(i + k + 1, n)
                    # Find the smallest character in the window [i, i+k]
                    for j in range(i, limit):
                        if arr[j] < smallest_char:
                            smallest_char = arr[j]
                            pos_of_smallest = j
                    # Move smallest_char to position i by rotating the sublist
                    # Construct sublist: arr[pos_of_smallest], arr[i:pos_of_smallest]
                    sublist = [arr[pos_of_smallest]] + arr[i:pos_of_smallest]
                    arr[i:pos_of_smallest + 1] = sublist
                    k -= pos_of_smallest - i
                    swap_occurred = True
                    break
            if not swap_occurred:
                break

        return "".join(arr)