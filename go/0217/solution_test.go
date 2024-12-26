package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected bool
	}{
		{
			name:     "Example 1",
			nums:     []int{1, 2, 3, 1},
			expected: true,
		},
		{
			name:     "Example 2",
			nums:     []int{1, 2, 3, 4},
			expected: false,
		},
		{
			name:     "Example 3",
			nums:     []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2},
			expected: true,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := containsDuplicate(tc.nums); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
