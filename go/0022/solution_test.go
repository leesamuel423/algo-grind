package solution

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input    int
		expected []string
	}{
		{
			name:     "Example 1",
			input:    3,
			expected: []string{"((()))", "(()())", "(())()", "()(())", "()()()"},
		},
		{
			name:     "Example 2",
			input:    1,
			expected: []string{"()"},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := generateParenthesis(tc.input); !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
