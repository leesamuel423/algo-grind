package solution

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		nums1    []int
		m        int
		nums2    []int
		n        int
		expected []int
	}{
		{
			name:     "Example 1",
			nums1:    []int{1, 2, 3, 0, 0, 0},
			m:        3,
			nums2:    []int{2, 5, 6},
			n:        3,
			expected: []int{1, 2, 2, 3, 5, 6},
		},
		{
			name:     "Example 2",
			nums1:    []int{1},
			m:        1,
			nums2:    []int{},
			n:        0,
			expected: []int{1},
		},
		{
			name:     "Example 3",
			nums1:    []int{0},
			m:        0,
			nums2:    []int{1},
			n:        1,
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			merge(tc.nums1, tc.m, tc.nums2, tc.n)
			if !reflect.DeepEqual(tc.expected, tc.nums1) {
				t.Errorf("Solution() = %v, want %v", tc.nums1, tc.expected)
			}
		})
	}
}
