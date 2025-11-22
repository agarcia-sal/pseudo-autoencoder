class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        self.sort_array(nums)
        sorted_nums = self.copy_array(nums)
        n = self.length_of_collection(nums)
        left = (n - 1) // 2
        right = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                nums[i] = sorted_nums[right]
                right -= 1

    def sort_array(self, collection: list[int]) -> None:
        collection.sort()

    def copy_array(self, collection: list[int]) -> list[int]:
        return collection[:]

    def length_of_collection(self, collection: list[int]) -> int:
        return len(collection)