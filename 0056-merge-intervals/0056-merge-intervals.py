class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by starting value
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            # If result is empty or no overlap
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                # Merge overlapping intervals
                if end > result[-1][1]:
                    result[-1][1] = end

        return result