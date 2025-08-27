def testPrefixSum(nums):
    newNums = [1] * len(nums)
    print(newNums)

    newNums[0] = nums[0]

    for x in range(1, len(nums)):
        newNums[x] = newNums[x-1]+nums[x]
        print(newNums, 'oppoo')

    print(newNums, 'lo')

testPrefixSum([1,2,3,4])