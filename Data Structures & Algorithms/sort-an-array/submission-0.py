class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i < len(left):
                res += left[i:]
            if j < len(right):
                res += right[j:]
            return res

        def merge_sort(nums, start, end):
            if start + 1 >= end:
                return nums[start:end]

            mid = (start + end) // 2
            left_arr = merge_sort(nums, start, mid)
            right_arr = merge_sort(nums, mid, end)
            return merge(left_arr, right_arr)
        
        return merge_sort(nums, 0, len(nums))