class Solution(object):
    def findClosestNumber(self, nums):
        tmp= min([abs(i) for i in nums])
        if tmp in nums:
            return tmp
        return -tmp
