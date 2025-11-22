class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        tasks = list(zip(plantTime, growTime))
        tasks.sort(key=lambda x: x[1], reverse=True)

        current_day = 0
        earliest_bloom = 0

        for plant, grow in tasks:
            current_day += plant
            earliest_bloom = max(earliest_bloom, current_day + grow)

        return earliest_bloom