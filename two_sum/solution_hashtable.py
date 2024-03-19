class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        hashmap = {}
        # add each element value as key
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        # check if difference of target and array value exists in table
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap and hashmap[difference] != i:
                return [i, hashmap[difference]]
