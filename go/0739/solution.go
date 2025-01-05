package solution

func dailyTemperatures(temperatures []int) []int {
	output := make([]int, len(temperatures))
	stack := make([]int, 0)

	for idx, temp := range temperatures {
		for len(stack) > 0 && temp > temperatures[stack[len(stack)-1]] {
			popped := stack[len(stack)-1]
			output[popped] = idx - popped
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, idx)
	}

	return output
}
