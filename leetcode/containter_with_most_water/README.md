# Intuition
My Initial solution was to brute force: Consider every possible pair of lines and calculate the area formed by these lines. Keep track of the maximum area found.

# Approach
Utilize two pointers, one starting from the beginning and the other from the end of the array representing the heights. Move the pointers towards each other, calculating the area based on the minimum height and maximum width.

# Complexity
- Time complexity:
O(n) time complexity as it involves a single pass through the array.

- Space complexity:
O(1), which means it uses constant extra space regardless of the input size.

# Code
```
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	maxWater := 0
	left, right := 0, len(height)-1

	for left < right {
		minHeight := min(height[left], height[right])
		distance := right - left
		area := distance * minHeight
		maxWater = max(maxWater, area)

		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return maxWater
}

```
