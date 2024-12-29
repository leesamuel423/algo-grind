package solution

import (
	"unicode"
)

func isPalindrome(s string) bool {
	runes := []rune(s)
	r := 0
	l := len(runes) - 1

	for r < l {
		for r < l && !unicode.IsNumber(runes[r]) && !unicode.IsLetter(runes[r]) {
			r += 1
		}
		for r < l && !unicode.IsNumber(runes[l]) && !unicode.IsLetter(runes[l]) {
			l -= 1
		}
		if unicode.ToLower(runes[r]) != unicode.ToLower(runes[l]) {
			return false
		}
		r += 1
		l -= 1
	}
	return true
}
