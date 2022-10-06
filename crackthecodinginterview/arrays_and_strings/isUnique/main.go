package main

import (
	"fmt"
	"isUnique/unique"
)

func main() {
	var text string = "Hello world"
	r := unique.IsUnique(text)
	fmt.Println(r)
}
