class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        max_satisfaction = 0
        current_satisfaction = 0
        total_satisfaction = 0
        for s in satisfaction:
            current_satisfaction += s
            total_satisfaction += current_satisfaction
            if total_satisfaction > max_satisfaction:
                max_satisfaction = total_satisfaction
        return max_satisfaction