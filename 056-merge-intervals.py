class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return newInterval
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] < newInterval[0]:
                if intervals[i + 1][0] < newInterval[0]:
                    i += 1
                    continue
                intervals.insert(i + 1, newInterval)
                i += 1
                break
            intervals[i][1] = newInterval[1]
            break
        j = i + 1
        while j < len(intervals):
            print(i, j, intervals)
            if newInterval[1] >= intervals[j][1]:
                intervals.pop(j)
            elif newInterval[1] >= intervals[j][0]:
                intervals[i][1] = intervals[j][1]
                intervals.pop(j)
                break
            else: break
        return intervals