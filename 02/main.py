inputs = list(map(int, open("./input.txt").read().split(",")))


def run_program(arr):
    def calc_opcode(op, x, y):
        return x + y if op == 1 else x * y

    def do_opcode(inp):
        op, x, y, z = inp

        if inp[0] == 99:
            return

        arr[z] = calc_opcode(op, arr[x], arr[y])

    for x in range(0, len(arr) - 1, 4):
        do_opcode(arr[x : x + 4])

    return arr[0]


# Part 1:
# inputs[1] = 12
# inputs[2] = 2
# print(run_program(inputs))

for x in range(100):
    for y in range(100):
        arr = inputs.copy()
        arr[1] = x
        arr[2] = y
        if run_program(arr) == 19690720:
            print(100 * x + y)
