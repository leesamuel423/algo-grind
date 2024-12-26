package solution

func containsDuplicate(nums []int) bool {
	cache := make(map[int]bool)
	for _, num := range nums {
		if cache[num] {
			return true
		}
		cache[num] = true
	}
	return false
}
