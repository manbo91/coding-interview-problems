"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given an array of integers. Return all the permutations of this array.

def permute(nums):
  # Fill this in.

print permute([1, 2, 3])
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
"""
import copy


def permute(nums):
    finalCompoundList = []

    if len(nums) == 0:
        finalCompoundList.append([])
    else:
        first_element = nums[0]
        after_first = slice(1, None)
        rest_list = nums[after_first]
        sub_compoundList = permute(rest_list)

        for aList in sub_compoundList:
            for j in range(0, len(aList) + 1):
                bList = copy.deepcopy(aList)
                bList.insert(j, first_element)

                finalCompoundList.append(bList)

    return finalCompoundList


print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
