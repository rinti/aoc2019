from itertools import permutations

inputs = list(map(int, open("./input.txt").read().split(",")))

def run_program(arr):
    i = 0

    def add(x, y, z, *args):
        arr[z] = arr[x] + arr[y]

    def mult(x, y, z, *args):
        arr[z] = arr[x] * arr[y]

    def put(x, *args):
        print("asdfa", x)
        arr[x] = 1
        # arr[x] = int(input())

    def printop(x, *args):
        print ("PRINT:")
        print(arr[x])

    OPS = {
        1: add,
        2: mult,
        3: put,
        4: printop,
    }

    def do_operation(op, i, x, y, z):
        x = i + 1 if x == 1 else arr[i + 1]
        y = i + 2 if y == 1 else arr[i + 2]
        z = i + 3 if z == 1 else arr[i + 3]

        OPS[op](x, y, z)

    while arr[i] != 99:
        instruction = f"{arr[i]:05}"  # Zero pad
        z, y, x, _, op = instruction

        do_operation(int(op), i, int(x), int(y), int(z))

        increment = 2 if int(op) in [3, 4] else 4
        i = i + increment

run_program(inputs)
