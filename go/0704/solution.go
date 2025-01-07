package solution

func search(nums []int, target int) int {
	p1 := 0
	p2 := len(nums) - 1

	for p1 <= p2 {
		mid := p1 + (p2-p1)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			p2 = mid - 1
		} else {
			p1 = mid + 1
		}
	}
	return -1
}
