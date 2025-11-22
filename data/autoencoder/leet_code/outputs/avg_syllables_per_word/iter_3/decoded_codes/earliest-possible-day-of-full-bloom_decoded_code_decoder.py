class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        tasks = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
        current_day = 0
        earliest_bloom = 0
        for plant, grow in tasks:
            current_day += plant
            earliest_bloom = max(earliest_bloom, current_day + grow)
        return earliest_bloom