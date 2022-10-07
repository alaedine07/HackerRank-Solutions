package main

import (
	"fmt"
	"string_compression/compress"
)

func main() {
	s := []byte{'a', 'b', 'b', 'a', 'a', 'c', 'c', 'b', 'v', 'v', 'v'}
	r := compress.Compress(s)
	fmt.Println(r)
}
