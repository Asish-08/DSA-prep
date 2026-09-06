# Last updated: 9/5/2026, 10:09:37 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort()

        max_rooms = 0
        current_rooms = 0

        for time, action in events:
            current_rooms += action
            max_rooms = max(max_rooms, current_rooms)
    
        return max_rooms