class Solution:
    def reversePairs(self, nums):
        def merge_and_count(nums, start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = merge_and_count(nums, start, mid) + merge_and_count(nums, mid + 1, end)

            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            merged = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    merged.append(nums[left])
                    left += 1
                else:
                    merged.append(nums[right])
                    right += 1

            merged.extend(nums[left:mid + 1])
            merged.extend(nums[right:end + 1])
            nums[start:end + 1] = merged

            return count

        return merge_and_count(nums, 0, len(nums) - 1)