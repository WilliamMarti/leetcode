class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        check = {}

        for x in nums:

            if x not in check:

                check[x] = 1

            else:

                check[x] = check[x] + 1

        for key, value in check.items():

            if value != 2:

                return key