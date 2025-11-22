class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = create_new_nums(nums, i, j)
                        for operation in (lambda: (lambda x,y: x/y), 
                                                  (lambda x,y: x*y), 
                                                  (lambda x,y: x+y), 
                                                  (lambda x,y: x-y))():
                            # To avoid duplicate calculations for addition and multiplication, enforce j > i
                            if (operation is (lambda x,y: x+y) or operation is (lambda x,y: x*y)) and j > i:
                                continue
                            if operation != (lambda x,y: x/y) or nums[j] != 0:
                                new_nums.append(operation(nums[i], nums[j]))
                                if solve(new_nums):
                                    return True
                                new_nums.pop()
            return False

        def create_new_nums(nums, i, j):
            return [nums[k] for k in range(len(nums)) if k != i and k != j]

        # We need to identify the exact functions for operations to do identity checks accurately.
        # Instead of lambda identity checks which won't work, define them once and use directly.

        def apply_operation(operation, v1, v2):
            if operation == 'div':
                return v1 / v2
            elif operation == 'mul':
                return v1 * v2
            elif operation == 'add':
                return v1 + v2
            elif operation == 'sub':
                return v1 - v2

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = create_new_nums(nums, i, j)
                        for op in ('div', 'mul', 'add', 'sub'):
                            if (op in ('add', 'mul') and j > i):
                                continue
                            if not (op == 'div' and nums[j] == 0):
                                new_nums.append(apply_operation(op, nums[i], nums[j]))
                                if solve(new_nums):
                                    return True
                                new_nums.pop()
            return False

        return solve(cards)