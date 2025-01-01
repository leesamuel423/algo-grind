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
			input:    []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
			expected: 6,
		},
		{
			name:     "Example 2",
			input:    []int{4, 2, 0, 3, 2, 5},
			expected: 9,
		},
		{
			name:     "Example 3",
			input:    []int{5, 5, 1, 7, 1, 1, 5, 2, 7, 6},
			expected: 23,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := trap(tc.input); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
