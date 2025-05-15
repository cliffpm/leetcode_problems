class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            curr = nums[i]
            diff = target - curr
            if diff in hashmap:
                return [hashmap.get(diff), i];
            hashmap[nums[i]] = i;
        return [-1,-1]
