package solution

func trap(height []int) int {
	p1 := 0
	p2 := len(height) - 1
	maxL := height[p1]
	maxR := height[p2]
	total := 0

	for p1 <= p2 {
		if maxL <= maxR {
			maxL = max(maxL, height[p1])
			total += maxL - height[p1]
			p1++
		} else {
			maxR = max(maxR, height[p2])
			total += maxR - height[p2]
			p2--
		}
	}
	return total
}
