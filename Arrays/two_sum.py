class Solution(object):
    def twoSum(curr, x, target):
        for i in range (len(x)):
            for j in range (i+1, len(x)):
                if x[j] == target - x[i]:
                    return [i,j]


        return []