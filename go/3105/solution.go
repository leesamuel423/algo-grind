package solution

func longestMonotonicSubarray(nums []int) int {
	longest := 1
	inc := 1
	dec := 1

	for i := 0; i < len(nums)-1; i++ {
		if nums[i] < nums[i+1] {
			inc += 1
			dec = 1
		} else {
			inc = 1
		}

		if nums[i] > nums[i+1] {
			dec += 1
			inc = 1
		} else {
			dec = 1
		}

		longest = max(inc, dec, longest)
	}

	return longest
}
