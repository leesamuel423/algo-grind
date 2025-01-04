package solution

func generateParenthesis(n int) []string {
	final := make([]string, 0)

	var generate func(string, int, int)
	generate = func(slate string, l int, r int) {
		if len(slate) == 2*n {
			final = append(final, slate)
		}
		if l > 0 {
			generate(slate+"(", l-1, r)
		}
		if l < r {
			generate(slate+")", l, r-1)
		}
	}

	generate("", n, n)
	return final
}
