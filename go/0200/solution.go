package solution

func numIslands(grid [][]byte) (island int) {
	var (
		dfs    func(int, int)
		rowLen = len(grid)
		colLen = len(grid[0])
	)

	dfs = func(r, c int) {
		if r < 0 || c < 0 || r == rowLen || c == colLen || grid[r][c] != '1' {
			return
		}
		grid[r][c] = '2'
		dfs(r, c+1)
		dfs(r, c-1)
		dfs(r+1, c)
		dfs(r-1, c)
	}

	for row := 0; row < rowLen; row++ {
		for col := 0; col < colLen; col++ {
			if grid[row][col] == '1' {
				island++
			}
			dfs(row, col)
		}
	}
	return
}
