package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		grid     [][]byte
		expected int
	}{
		{
			name: "Example 1",
			grid: [][]byte{
				{'1', '1', '1', '1', '0'},
				{'1', '1', '0', '1', '0'},
				{'1', '1', '0', '0', '0'},
				{'0', '0', '0', '0', '0'},
			},
			expected: 1,
		},
		{
			name: "Example 2",
			grid: [][]byte{
				{'1', '1', '0', '0', '0'},
				{'1', '1', '0', '0', '0'},
				{'0', '0', '1', '0', '0'},
				{'0', '0', '0', '1', '1'},
			},
			expected: 3,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := numIslands(tc.grid); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
