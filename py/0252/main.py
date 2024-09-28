from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        prev_end = 0
        for i in intervals:
            start, end = i
            if prev_end > start:
                return False
            prev_end = end
        return True
