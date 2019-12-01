package main

import (
    "io/ioutil"
    "fmt"
    "strings"
    "math"
    "strconv"
)

func mass_to_fuel(mass string) int {
    m, _ := strconv.Atoi(mass)
    return int(math.Floor(float64(m) / 3) - 2)
}

func main() {
    input, err := ioutil.ReadFile("./input.txt")

    if err != nil {
        panic(err)
    }

    lines := strings.Split(string(input), "\n")
    lines = lines[:len(lines)-1]

    var total int = 0

    for _, line := range lines {
        if line == "\n" {
            continue
        }
        total = total + mass_to_fuel(line)
    }

    fmt.Println(total)
}
