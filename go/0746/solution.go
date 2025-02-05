package solution

func minCostClimbingStairs(cost []int) int {
	length := len(cost)
	for i := 2; i < length; i++ {
		cost[i] = cost[i] + min(cost[i-1], cost[i-2])
	}
	return min(cost[length-1], cost[length-2])
}
