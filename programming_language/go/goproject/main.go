package main

import (
	"flag"
	"fmt"
	"runtime"
)

var (
	help        = flag.Bool("h", false, "to show help")
	showVersion = flag.Bool("v", false, "to show version of project")
	showVerbose = flag.Bool("V", false, "to show verbose information about project")
)

// go编译的时候使用
var version string
var commit string

//main
func main() {
	fmt.Println("Hello world!")
	flag.Parse()
	if *help {
		flag.PrintDefaults()
		return
	}
	if *showVersion {
		fmt.Printf("project version: %s\n", version)
		return
	}
	if *showVerbose {
		fmt.Printf("project version: %s\n", version)
		fmt.Printf("go version: %s\n", runtime.Version())
		fmt.Printf("git commit: %s\n", commit)
		return
	}
}
