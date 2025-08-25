# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Solution 1
def canPlaceFlowersSolution1(flowerbed: list[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True
    return count >= n

# Solution 2
def canPlaceFlowersSolution2(flowerbed: list[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
    i = 0

    while i < length:
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True
                i += 1  # Skip the next plot since we just planted a flower
        i += 1

    return count >= n

# Solution 3
def canPlaceFlowersSolution3(flowerbed: list[int], n: int) -> bool:
    flowerbed = [0] + flowerbed + [0]  # Add padding to avoid boundary checks
    count = 0

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True

    return count >= n

# Solution 4
def canPlaceFlowersSolution4(flowerbed: list[int], n: int) -> bool:
    plantedNo = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if i == 0:
                leftItem = flowerbed[i]
            else:
                leftItem = flowerbed[i - 1]
            if i < len(flowerbed) - 1:
                rightItem = flowerbed[i+1]
            else:
                rightItem = flowerbed[i]
            
            if leftItem == 0 and rightItem == 0:
                plantedNo += 1
                flowerbed[i] = 1
    
    return plantedNo >= n


flowerbed = [1, 0, 0, 0, 1]
n = 2
print(canPlaceFlowersSolution1(flowerbed, n))  # Output: True
print(canPlaceFlowersSolution2(flowerbed, n))  # Output: True
print(canPlaceFlowersSolution3(flowerbed, n))  # Output: True
print(canPlaceFlowersSolution4(flowerbed, n))  # Output: True


