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
			input:    []int{10, 15, 20},
			expected: 15,
		},
		{
			name:     "Example 2",
			input:    []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1},
			expected: 6,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := minCostClimbingStairs(tc.input); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
