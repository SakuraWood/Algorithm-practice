def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length=len(nums)
    if length==1:
        return nums[0]
    else:
        a=nums[0:1]
        b=nums[1:length]
        if maxSubArray(a)+maxSubArray(b)<maxSubArray(b) and maxSubArray(a)<maxSubArray(b):
            result = maxSubArray(b)
        if maxSubArray(a)+maxSubArray(b)<maxSubArray(a) and maxSubArray(a)>maxSubArray(b):
            result = maxSubArray(a)
        else:
            result = maxSubArray(a)+maxSubArray(b)
        return result

# print maxSubArray([1,2,-4,3,4,-2,7,5,-41])


def max(nums):
    length=len(nums)
    a=nums[0:length-1]
    b=nums[1:length]

    if sum(nums)<(sum(a)+sum(b)) and sum(a)<sum(b):
        return max(b)
    elif sum(nums)<(sum(a)+sum(b)) and sum(a)>sum(b):
        return max(a)
    else:
        return sum(nums)

print max([1,2,-4,3,4,-2,7,5,-41])

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m==1:
        return 1
    if n==1:
        return 1
    dp=[[0 for i in range(n)] for i in range(m)]
    dp[0]=[1]*n
    for x in range(m):
        dp[x][0]=1
    for x in range(1,m):
        for y in range(1,n):
            dp[x][y]=dp[x-1][y]+dp[x][y-1]
    return dp[m-1][n-1]
print uniquePaths(4,4)