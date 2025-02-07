package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		s1       string
		s2       string
		expected bool
	}{
		{
			name:     "Example 1",
			s1:       "bank",
			s2:       "kanb",
			expected: true,
		},
		{
			name:     "Example 2",
			s1:       "attack",
			s2:       "defend",
			expected: false,
		},
		{
			name:     "Example 3",
			s1:       "kelb",
			s2:       "kelb",
			expected: true,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := areAlmostEqual(tc.s1, tc.s2); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
