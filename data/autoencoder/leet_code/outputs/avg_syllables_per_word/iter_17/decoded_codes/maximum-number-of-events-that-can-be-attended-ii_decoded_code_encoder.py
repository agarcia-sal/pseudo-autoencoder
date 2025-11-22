from bisect import bisect_right
from typing import List, Tuple

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # SortEventsByEndDay: sort events by their end day
        events.sort(key=lambda x: x[1])
        number_of_events = len(events)

        # InitializeDPTable(number_of_events, k): create (number_of_events+1) x (k+1) dp table with zeros
        dp_table = [[0] * (k + 1) for _ in range(number_of_events + 1)]

        # Pre-extract end days to assist binary search for FindLatestNonOverlappingEvent
        end_days = [event[1] for event in events]

        # To speed up FindLatestNonOverlappingEvent, we will use binary search on end_days
        for index in range(1, number_of_events + 1):
            start_day, end_day, event_value = events[index - 1]

            # FindLatestNonOverlappingEvent(events, start_day):
            # latest event that ends before start_day
            # We need to find rightmost end_day < start_day
            # bisect_right returns insertion point, so previous index is that -1
            previous_event_index = bisect_right(end_days, start_day - 1)

            for count in range(1, k + 1):
                without_current_event = dp_table[index - 1][count]
                with_current_event = dp_table[previous_event_index][count - 1] + event_value
                dp_table[index][count] = max(without_current_event, with_current_event)

        return dp_table[number_of_events][k]