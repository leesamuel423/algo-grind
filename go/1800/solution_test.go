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
			input:    []int{10, 20, 30, 5, 10, 50},
			expected: 65,
		},
		{
			name:     "Example 2",
			input:    []int{10, 20, 30, 40, 50},
			expected: 150,
		},
		{
			name:     "Example 3",
			input:    []int{12, 17, 15, 13, 10, 11, 12},
			expected: 33,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := maxAscendingSum(tc.input); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
