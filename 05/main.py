from itertools import permutations

inputs = list(map(int, open("./input.txt").read().split(",")))

def run_program(arr):
    i = 0

    def add(i, x, y, z, *args):
        arr[z] = arr[x] + arr[y]
        return False, 4

    def mult(i, x, y, z, *args):
        arr[z] = arr[x] * arr[y]
        return False, 4

    def put(i, x, *args):
        print ("INPUT >> ")
        arr[x] = int(input())
        return False, 2

    def printop(i, x, *args):
        print ("PRINT:")
        print(arr[x])
        return False, 2

    def jump_if_true(i, x, y, *args):
        if arr[x] != 0:
            return True, arr[y]
        return False, 3

    def jump_if_false(i, x, y, *args):
        if arr[x] == 0:
            return True, arr[y]
        return False, 3

    def lt(i, x, y, z, *args):
        if arr[x] < arr[y]:
            arr[z] = 1
        else:
            arr[z] = 0
        return False, 4

    def eq(i, x, y, z, *args):
        if arr[x] == arr[y]:
            arr[z] = 1
        else:
            arr[z] = 0
        return False, 4

    OPS = {
        1: add,
        2: mult,
        3: put,
        4: printop,
        5: jump_if_true,
        6: jump_if_false,
        7: lt,
        8: eq,
    }

    def do_operation(op, i, x, y, z):
        x = i + 1 if x == 1 else arr[i + 1]
        y = i + 2 if y == 1 else arr[i + 2]
        z = i + 3 if z == 1 else arr[i + 3]

        return OPS[op](i, x, y, z)

    while arr[i] != 99:
        instruction = f"{arr[i]:05}"  # Zero pad
        z, y, x, _, op = instruction

        reset_pointer, increment = do_operation(int(op), i, int(x), int(y), int(z))

        if reset_pointer:
            i = increment
        else:
            i = i + increment

run_program(inputs)
