class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s = 0               # start index
        e = len(nums) - 1   # ending index

        while s <= e:

            m = (s + e) // 2

            if nums[m] == target:

                return m

            elif nums[m] < target:

                s = m + 1

            elif nums[m] > target:

                e = m - 1

        return -1