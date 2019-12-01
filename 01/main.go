package main

import (
    "io/ioutil"
    "fmt"
    "strings"
    "math"
    "strconv"
)

func mass_to_fuel(mass int) int {
    return int(math.Floor(float64(mass) / 3) - 2)
}

func total_mass_to_fuel(mass int, acc int) int {
    var fuel int = mass_to_fuel(mass)

    if fuel <= 0 {
        return acc
    } else {
        return total_mass_to_fuel(fuel, acc + fuel)
    }
}

func main() {
    input, err := ioutil.ReadFile("./input.txt")

    if err != nil {
        panic(err)
    }

    lines := strings.Split(string(input), "\n")
    lines = lines[:len(lines)-1]

    var total int = 0
    var mass int;

    for _, line := range lines {
        if line == "\n" {
            continue
        }
        mass, _ = strconv.Atoi(line)
        // to solve problem 1 switch total_mass_to_fuel to mass_to_fuel without second arg
        total = total + total_mass_to_fuel(mass, 0)
    }

    fmt.Println(total)
}
