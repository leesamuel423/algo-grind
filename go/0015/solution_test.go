package solution

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected [][]int
	}{
		{
			name: "Example 1",
			nums: []int{-1, 0, 1, 2, -1, -4},
			expected: [][]int{
				{-1, -1, 2},
				{-1, 0, 1},
			},
		},
		{
			name:     "Example 2",
			nums:     []int{0, 1, 1},
			expected: [][]int{},
		},
		{
			name: "Example 3",
			nums: []int{0, 0, 0},
			expected: [][]int{
				{0, 0, 0},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := threeSum(tc.nums); !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
