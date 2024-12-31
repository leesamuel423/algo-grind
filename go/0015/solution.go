package solution

import (
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	output := make([][]int, 0)
	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		target := -nums[i]
		pairs := helper(nums[i+1:], target)
		for _, pair := range pairs {
			output = append(output, []int{nums[i], pair[0], pair[1]})

		}
	}
	return output

}

func helper(nums []int, target int) [][]int {
	result := make([][]int, 0)
	l := 0
	r := len(nums) - 1

	for l < r {
		sum := nums[l] + nums[r]
		if sum == target {
			result = append(result, []int{nums[l], nums[r]})
			for l < r && nums[l] == nums[l+1] {
				l++
			}
			for l < r && nums[r] == nums[r-1] {
				r--
			}
			l++
			r--
		} else if sum > target {
			r--
		} else {
			l++
		}
	}
	return result
}

