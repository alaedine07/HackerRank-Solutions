package main

import (
	"fmt"
	"palindrome_permutations/palindrome"
)

func main() {
	text := "add"
	r := palindrome.IsPalindromePerm(text)
	fmt.Println(r)
}
