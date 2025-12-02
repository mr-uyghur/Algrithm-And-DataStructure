# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

#  Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2-pointer approach.
        #left pointer at the start of the array
        #right pointer at the end of the array
        #move the pointer that points to the lower line
        #calculate the amount of water each step, keep track of it with a var
        #if height[left_pointer] <= height[right_pointer] increase left pointer by 1
        #if height[left_pointer] > height[right_pointer] decrease right pointer by 1
        #calculate the area before each change and keep track of the maximum area
        #end the loop when 2 pointers are equal to each other
        #area = width * height
        left = 0
        right = len(height) -1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area =  width * h
            max_area = max( area, max_area) 

            if height[left] <= height[right]:
                left +=1
            else:
                right -= 1

        return max_area

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic example
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49, "Test 1 Failed"
    print("✓ Test 1 Passed: example returns 49")

    # Test Case 2: Two equal heights
    assert solution.maxArea([1,1]) == 1, "Test 2 Failed"
    print("✓ Test 2 Passed: [1,1] returns 1")

    # Test Case 3: Monotonic decreasing
    assert solution.maxArea([5,4,3,2,1]) == 6, "Test 3 Failed"
    print("✓ Test 3 Passed: monotonic decreasing returns 6")

    # Test Case 4: Monotonic increasing
    assert solution.maxArea([1,2,3,4,5]) == 6, "Test 4 Failed"
    print("✓ Test 4 Passed: monotonic increasing returns 6")

    # Test Case 5: Plateau
    assert solution.maxArea([4,4,4,4]) == 12, "Test 5 Failed"
    print("✓ Test 5 Passed: plateau returns 12")

    # Test Case 6: Small peak
    assert solution.maxArea([1,2,1]) == 2, "Test 6 Failed"
    print("✓ Test 6 Passed: small peak returns 2")

    # Test Case 7: Single element
    assert solution.maxArea([7]) == 0, "Test 7 Failed"
    print("✓ Test 7 Passed: single element returns 0")

    # Test Case 8: Two elements (different heights)
    assert solution.maxArea([2,9]) == 2, "Test 8 Failed"
    print("✓ Test 8 Passed: [2,9] returns 2")

    # Test Case 9: Large symmetric edges
    arr = [100] + [1]*100 + [100]
    # best area is between the two 100s at the ends: width 101 * 100 = 10100
    assert solution.maxArea(arr) == 10100, "Test 9 Failed"
    print("✓ Test 9 Passed: large symmetric edges returns 10100")

    # Test Case 10: Wider block of tall heights with small edges
    # array: [1] + [100]*50 + [1] -> best between first and last 100 at indices 1 and 50
    # width = 50-1 = 49 -> area = 49 * 100 = 4900
    assert solution.maxArea([1] + [100]*50 + [1]) == 4900, "Test 10 Failed"
    print("✓ Test 10 Passed: wide block of tall heights returns 4900")

    # Test Case 11: Mixed heights
    assert solution.maxArea([3,1,2,4,5,2]) == 12, "Test 11 Failed"
    print("✓ Test 11 Passed: mixed heights returns 12")

    # Test Case 12: zeros included
    assert solution.maxArea([0,0,5,0,0]) == 0, "Test 12 Failed"
    print("✓ Test 12 Passed: zeros handled")

    print("\n✅ All test cases passed!")



        