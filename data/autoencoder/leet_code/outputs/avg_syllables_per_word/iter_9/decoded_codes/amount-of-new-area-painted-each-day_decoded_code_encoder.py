class Solution:
    def amountPainted(self, paint):
        max_end = max(end for _, end in paint)
        painted = [-1] * (max_end + 1)
        worklog = []

        for start, end in paint:
            current = start
            new_paint = 0
            while current < end:
                if painted[current] == -1:
                    painted[current] = end
                    new_paint += 1
                    current += 1
                else:
                    current = painted[current]
            worklog.append(new_paint)

        return worklog