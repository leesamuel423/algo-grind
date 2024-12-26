package solution

func isAnagram(s string, t string) bool {
	dict := make(map[rune]int)

	for _, letter := range s {
		dict[letter] += 1
	}

	for _, letter := range t {
		dict[letter] -= 1
		if dict[letter] < 0 {
			return false
		} else if dict[letter] == 0 {
			delete(dict, letter)
		}
	}

	return len(dict) == 0

}
