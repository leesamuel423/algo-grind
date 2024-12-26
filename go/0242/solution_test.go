package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		t        string
		expected bool
	}{
		{
			name:     "Example 1",
			s:        "anagram",
			t:        "nagaram",
			expected: true,
		},
		{
			name:     "Example 2",
			s:        "rat",
			t:        "car",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := isAnagram(tc.s, tc.t); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
