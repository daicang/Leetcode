class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        rooms = []
        intervals.sort()

        for start, end in intervals:
            has_room = False
            for i, room_end in enumerate(rooms):
                if room_end <= start:
                    rooms[i] = end
                    has_room = True
                    break

            if not has_room:
                rooms.append(end)

        return len(rooms)

