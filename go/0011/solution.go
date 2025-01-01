package solution

func maxArea(height []int) int {
	maxHeight := 0
	p1 := 0
	p2 := len(height) - 1
	for p1 < p2 {
		currVolume := min(height[p1], height[p2]) * (p2 - p1)
		maxHeight = max(maxHeight, currVolume)
		if height[p2] < height[p1] {
			p2--
		} else {
			p1++
		}
	}
	return maxHeight
}
