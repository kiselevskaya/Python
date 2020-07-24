

class Solution:

    def two_sum(self, nums: list, target: int):
        '''
        :param nums: list of integers
        :param target: integer
        :return: list of integers (indices)
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        Assume that each input would have exactly one solution, and you may not use the same element twice.
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.two_sum([0, 4, 3, 0], 0))  # [0, 3]
    print(solution.two_sum([-3, 4, 3, 90], 0))  # [0, 2]
