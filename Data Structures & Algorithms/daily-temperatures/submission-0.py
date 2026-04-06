class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force - for each day, scan rest of list until we hit warmer day
        result = []
        for i, temp in enumerate(temperatures):
            
            j = i + 1
            found = False
            while j < len(temperatures):
                if temperatures[j] > temp:
                    found = True
                    break
                j += 1

            if found:
                result.append(j - i)
            else:
                result.append(0)

        return result
