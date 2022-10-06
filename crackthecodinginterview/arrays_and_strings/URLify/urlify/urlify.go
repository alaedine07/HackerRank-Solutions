package urlify

import "strings"

func Urlify(text string) string {
	trimmed := strings.ReplaceAll(text, " ", "%")
	return trimmed
}
