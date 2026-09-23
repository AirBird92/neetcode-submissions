class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        num_set = set()
        while r < len(nums):
            if nums[r] in num_set:
                return True
            num_set.add(nums[r])
            r += 1
            if r > k:
                num_set.remove(nums[l])
                l += 1
        return False