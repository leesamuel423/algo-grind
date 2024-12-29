package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		s        string
		expected bool
	}{
		{
			name:     "Example 1",
			s:        "A man, a plan, a canal: Panama",
			expected: true,
		},
		{
			name:     "Example 2",
			s:        "race a car",
			expected: false,
		},
		{
			name:     "Example 3",
			s:        " ",
			expected: true,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := isPalindrome(tc.s); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
