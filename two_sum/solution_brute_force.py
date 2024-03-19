# Time complexity: O(n^2). For each element, we try to find 
# its complement by looping through the rest of the array 
# which takes O(n)O(n) time. Therefore, the time complexity is O(n^2)O(n).

# Space complexity: O(1)O(1). The space required 
# does not depend on the size of the input array, 
# so only constant space is used.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                    return indices
