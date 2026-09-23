class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        reverse_index = defaultdict(set)
        for i in range(len(nums)):
            indexes = reverse_index[nums[i]]
            for j in range(k + 1):
                if i - j in indexes:
                    return True
            reverse_index[nums[i]].add(i)
        return False