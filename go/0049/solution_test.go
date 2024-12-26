package solution

import (
	"slices"
	"strings"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		strs     []string
		expected [][]string
	}{
		{
			name: "Example 1",
			strs: []string{"eat", "tea", "tan", "ate", "nat", "bat"},
			expected: [][]string{
				{"tan", "nat"},
				{"bat"},
				{"eat", "tea", "ate"},
			},
		},
		{
			name: "Example 2",
			strs: []string{""},
			expected: [][]string{
				{""},
			},
		},
		{
			name: "Example 3",
			strs: []string{"a"},
			expected: [][]string{
				{"a"},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := groupAnagrams(tc.strs); !compareAnagramGroups(got, tc.expected) {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}

func compareAnagramGroups(got, want [][]string) bool {
	if len(got) != len(want) {
		return false
	}

	// Sort each group to normalize them
	for i := range got {
		slices.Sort(got[i])
	}
	for i := range want {
		slices.Sort(want[i])
	}

	// Convert each group to string for easier comparison
	gotStrs := make([]string, len(got))
	wantStrs := make([]string, len(want))

	for i := range got {
		gotStrs[i] = strings.Join(got[i], ",")
	}
	for i := range want {
		wantStrs[i] = strings.Join(want[i], ",")
	}

	slices.Sort(gotStrs)
	slices.Sort(wantStrs)

	return slices.Equal(gotStrs, wantStrs)
}
