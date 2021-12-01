class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return [newInterval]
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                if i + 1 < len(intervals) and intervals[i + 1][0] < newInterval[0]:
                    i += 1
                    continue
                intervals.insert(i + 1, newInterval)
                i += 1
                break
            if intervals[i][0] < newInterval[1]:
                intervals[i][0] = min(intervals[i][0], newInterval[0])
                intervals[i][1] = max(intervals[i][1], newInterval[1])
            else:
                intervals.insert(i, newInterval)
            break
        j = i + 1
        while j < len(intervals):
            if newInterval[1] >= intervals[j][1]:
                intervals.pop(j)
            elif newInterval[1] >= intervals[j][0]:
                intervals[i][1] = intervals[j][1]
                intervals.pop(j)
                break
            else: break
        return intervals