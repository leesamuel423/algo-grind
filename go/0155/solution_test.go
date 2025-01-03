package solution

import "testing"

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		ops      []string
		args     [][]int
		expected []int
	}{
		{
			name:     "Example 1",
			ops:      []string{"MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"},
			args:     [][]int{{}, {-2}, {0}, {-3}, {}, {}, {}, {}},
			expected: []int{0, 0, 0, 0, -3, 0, 0, -2},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			var stack MinStack
			var result []int

			for i, op := range tc.ops {
				switch op {
				case "MinStack":
					stack = Constructor()
					result = append(result, 0)
				case "push":
					stack.Push(tc.args[i][0])
					result = append(result, 0)
				case "pop":
					stack.Pop()
					result = append(result, 0)
				case "top":
					result = append(result, stack.Top())
				case "getMin":
					result = append(result, stack.GetMin())
				}
			}

			for i, v := range tc.expected {
				if result[i] != v {
					t.Errorf("Operation %d: got %v, want %v", i, result[i], v)
				}
			}
		})
	}
}
