package solution

func isValid(s string) bool {
	dict := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}
	stack := make([]rune, 0)

	for _, char := range s {
		if char == '(' || char == '[' || char == '{' {
			stack = append(stack, char)
		} else {
			if len(stack) == 0 {
				return false
			}
			x := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if dict[char] != x {
				return false
			}
		}
	}

	return len(stack) == 0
}
