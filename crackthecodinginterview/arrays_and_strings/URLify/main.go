package main

import (
	"fmt"
	"urlify/urlify"
)

func main() {
	text := "his name is johncena"
	r := urlify.Urlify(text)
	fmt.Println(r)
}
