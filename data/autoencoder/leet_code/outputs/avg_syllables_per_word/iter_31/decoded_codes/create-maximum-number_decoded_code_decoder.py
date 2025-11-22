from typing import List

class Solution:
    class ListNode:
        def __init__(self, val: int = 0, next: 'Solution.ListNode' = None):
            self.val = val
            self.next = next

    @staticmethod
    def list_to_linkedlist(nums: List[int]) -> 'Solution.ListNode':
        dummy = Solution.ListNode()
        current = dummy
        for num in nums:
            current.next = Solution.ListNode(num)
            current = current.next
        return dummy.next

    @staticmethod
    def linkedlist_to_list(head: 'Solution.ListNode') -> List[int]:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    @staticmethod
    def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def maxSingleArray(nums: List[int], k: int) -> List[int]:
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            merged_list = []
            i, j = 0, 0
            len1, len2 = len(arr1), len(arr2)

            while i < len1 or j < len2:
                # Compare remaining slices lexicographically
                if arr1[i:] > arr2[j:]:
                    merged_list.append(arr1[i])
                    i += 1
                else:
                    merged_list.append(arr2[j])
                    j += 1
            return merged_list

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and (k - i) <= len2:
                subseq1 = maxSingleArray(nums1, i)
                subseq2 = maxSingleArray(nums2, k - i)
                candidate = merge(subseq1, subseq2)
                if candidate > max_number:
                    max_number = candidate
        return max_number