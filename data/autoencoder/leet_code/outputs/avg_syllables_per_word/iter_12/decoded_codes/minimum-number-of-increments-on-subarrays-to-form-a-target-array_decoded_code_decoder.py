class Solution:
    def minNumberOperations(self, target):
        operations = 0
        previous = 0
        for current in target:
            if current > previous:
                operations += current - previous
            previous = current
        return operations