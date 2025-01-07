package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		target   int
		expected int
	}{
		{
			name:     "Example 1",
			input:    []int{-1, 0, 3, 5, 9, 12},
			target:   9,
			expected: 4,
		},
		{
			name:     "Example 2",
			input:    []int{-1, 0, 3, 5, 9, 12},
			target:   2,
			expected: -1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := search(tc.input, tc.target); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
