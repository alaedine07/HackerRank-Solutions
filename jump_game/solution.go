func canJump(nums []int) bool {
    maxReach := 0
    for i := 0; i < len(nums)-1; i++ {
        if i > maxReach {
            return false
        }
        maxReach = max(maxReach, i+nums[i])
    }
    return maxReach >= len(nums)-1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
