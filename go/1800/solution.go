package solution

func maxAscendingSum(nums []int) int {
	output := nums[0]
	currMax := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			currMax += nums[i]
		} else {
			output = max(output, currMax)
			currMax = nums[i]
		}
	}
	return max(output, currMax)
}
