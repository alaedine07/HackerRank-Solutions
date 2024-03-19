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
