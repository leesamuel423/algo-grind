package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "Example 1",
			input:    "()",
			expected: true,
		},
		{
			name:     "Example 2",
			input:    "{}()[]",
			expected: true,
		},
		{
			name:     "Example 3",
			input:    "(]",
			expected: false,
		},
		{
			name:     "Example 3",
			input:    "([])",
			expected: true,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := isValid(tc.input); got != tc.expected {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}
