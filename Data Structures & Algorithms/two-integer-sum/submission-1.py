class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for index,i in enumerate(nums):
            comp=target-i
            if comp in map1:
                return [map1[comp],index]
            map1[i]=index