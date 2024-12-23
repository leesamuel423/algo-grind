package solution

func merge(nums1 []int, m int, nums2 []int, n int) {
	curr := len(nums1) - 1
	m -= 1
	n -= 1
	for n >= 0 {
		if m >= 0 && nums1[m] > nums2[n] {
			nums1[curr] = nums1[m]
			m--
		} else {
			nums1[curr] = nums2[n]
			n--
		}
		curr--
	}
}

// O(n) time solve
/*
[1, 2, 3, 0, 0, 0], [2, 5, 6]

[1, 2, 3, 0, 0, 0]
       3                    6
[1, 2, 3, 0, 0, 6]
       3                5
[1, 2, 3, 0, 5, 6]
       3                2
[1, 2, 0, 3, 5, 6]
    2                   2
[1, 2, 2, 3, 5, 6]

move backwards, pointer m, n, curr
*/
