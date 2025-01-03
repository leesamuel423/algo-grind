package solution

type MinStack struct {
	stack    []int
	minstack []int
}

func Constructor() MinStack {
	stack := make([]int, 0)
	minstack := make([]int, 0)
	return MinStack{stack: stack, minstack: minstack}
}

func (this *MinStack) Push(val int) {
	if len(this.stack) == 0 {
		this.minstack = append(this.minstack, val)
	} else {
		this.minstack = append(this.minstack, min(this.minstack[len(this.minstack)-1], val))
	}
	this.stack = append(this.stack, val)
}

func (this *MinStack) Pop() {
	if len(this.stack) > 0 {
		this.stack = this.stack[:len(this.stack)-1]
		this.minstack = this.minstack[:len(this.minstack)-1]
	}
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.minstack[len(this.minstack)-1]
}
