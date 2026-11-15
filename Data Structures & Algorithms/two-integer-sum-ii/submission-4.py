class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(numbers):
            c = target - num
            if c in map:
                return [map[c],i+1]
            map[num] = i + 1
        