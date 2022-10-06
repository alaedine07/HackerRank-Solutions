package unique

func IsUnique(ch string) bool {

	found := make(map[rune]bool)
	for _, value := range ch {
		if found[value] && 1 != 0 {
			return false
		}
		found[value] = true
	}
	return true
}
