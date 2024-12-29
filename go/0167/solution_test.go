package solution

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		target   int
		expected []int
	}{
		{
			name:     "Example 1",
			input:    []int{2, 7, 11, 15},
			target:   9,
			expected: []int{1, 2},
		},
		{
			name:     "Example 2",
			input:    []int{2, 3, 4},
			target:   6,
			expected: []int{1, 3},
		},
		{
			name:     "Example 3",
			input:    []int{-1, 0},
			target:   -1,
			expected: []int{1, 2},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := twoSum(tc.input, tc.target); !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
