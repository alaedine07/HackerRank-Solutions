package permute

import (
	"reflect"
	"sort"
	"strings"
)

func IsPermutation(ch_1 string, ch_2 string) bool {
	strs_1 := strings.Split(ch_1, "")
	sort.Strings(strs_1)
	strs_2 := strings.Split(ch_2, "")
	sort.Strings(strs_2)
	if reflect.DeepEqual(strs_1, strs_2) {
		return true
	}
	return false
}
