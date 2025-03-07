package solution

func twoSum(numbers []int, target int) []int {
	r := len(numbers) - 1
	l := 0

	for l < r {
		sum := numbers[l] + numbers[r]
		if sum == target {
			return []int{l + 1, r + 1}
		}
		if sum < target {
			l += 1
		} else {
			r -= 1
		}
	}
	return nil
}
