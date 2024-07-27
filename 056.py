class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        start = intervals[0][0]
        i = 1
        while i < len(intervals):
            if intervals[i][0] >= intervals[i-1][0] and intervals[i][1] <= intervals[i-1][1]:
                del intervals[i]

                continue
            if intervals[i][0] > intervals[i-1][1]:
                output.append([start, intervals[i-1][1]])
                if i < len(intervals):
                    start = intervals[i][0]
            i+=1
        output.append([start, intervals[-1][1]])
        return output
