class Solution:
    def search(self, nums, target):

        s = 0               # start index
        e = len(nums) - 1   # ending index

        while s <= e:

            middle_index = (s + e) // 2

            print(f"{s}")
            print(f"{e}")
            print(f"{middle_index}")
            test = nums[s:e]
            print(f"{test}")

            if nums[middle_index] == target:

                return middle_index

            elif nums[middle_index] < target:

                s = middle_index + 1

            elif nums[middle_index] > target:

                e = middle_index - 1

            # if we didn't catch it earlier, not found


            print("----------------")


        return -1

solution = Solution()

print(solution.search([-1,0,3,5,9,12], 9) == 4)
print("________________________________________________")

print(solution.search([-1,0,3,5,9,12], 2) == -1)
print("________________________________________________")

print(solution.search([5], -5) == -1)
print("________________________________________________")

print(solution.search([2,5], 5) == 1)
print("________________________________________________")

print(solution.search([2,5], 2) == 0)
print("________________________________________________")

print(solution.search([2,5], 0) == -1)
print("________________________________________________")

print(solution.search([-1,0,3,5,9,12], -1) == 0)
print("________________________________________________")