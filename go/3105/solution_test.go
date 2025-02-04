package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "Example 1",
			input:    []int{1, 4, 3, 3, 2},
			expected: 2,
		},
		{
			name:     "Example 2",
			input:    []int{3, 3, 3, 3},
			expected: 1,
		},
		{
			name:     "Example 3",
			input:    []int{3, 2, 1},
			expected: 3,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := longestMonotonicSubarray(tc.input); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
