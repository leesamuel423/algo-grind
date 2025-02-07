package solution

func areAlmostEqual(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	diffs := make([]int, 0, 2)

	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			diffs = append(diffs, i)
		}
	}

	if len(diffs) == 0 {
		return true
	}

	if len(diffs) != 2 {
		return false
	}

	if s1[diffs[0]] == s2[diffs[1]] && s1[diffs[1]] == s2[diffs[0]] {
		return true
	} else {
		return false
	}
}
