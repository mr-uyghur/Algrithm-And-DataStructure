# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

def maxArea( height):
    i, j, max_water = 0, len(height) - 1, 0
        
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(height[i], height[j]))
            
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return max_water

print(maxArea([1,8,6,2,5,4,8,3,7]))