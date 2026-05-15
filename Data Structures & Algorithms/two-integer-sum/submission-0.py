class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_diff_map = {}
        for idx, num in enumerate(nums):
            if num in seen_diff_map:
                return [seen_diff_map[num], idx]
            seen_diff_map[target - num] = idx