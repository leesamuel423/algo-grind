package solution

import (
	"slices"
)

func groupAnagrams(strs []string) [][]string {
	output := make([][]string, 0, len(strs))
	cache := make(map[string][]string)

	for _, word := range strs {
		chars := []rune(word)
		slices.Sort(chars)
		key := string(chars)
		cache[key] = append(cache[key], word)
	}

	for _, values := range cache {
		output = append(output, values)
	}

	return output
}
