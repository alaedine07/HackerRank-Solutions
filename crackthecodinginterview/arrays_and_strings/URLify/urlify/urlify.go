package urlify

import "strings"

func Urlify(text string) string {
	trimmed := strings.ReplaceAll(text, " ", "%20")
	return trimmed
}
