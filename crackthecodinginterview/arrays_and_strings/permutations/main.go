package main

import (
	"fmt"
	"permutations/isPermute"
)

func main() {
	ch_1 := "god"
	ch_2 := "dog"

	r := permute.IsPermutation(ch_1, ch_2)
	fmt.Println(r)
}
