inputs = list(map(int, open('./input.txt').read().split(',')))
inputs[1] = 12
inputs[2] = 2

def calc_opcode(op, x, y):
    return x + y if op == 1 else x * y

def do_opcode(arr):
    op, x, y, z = arr

    if arr[0] == 99:
        return

    inputs[z] = calc_opcode(op, inputs[x], inputs[y])

for x in range(0, len(inputs)-1, 4):
    do_opcode(inputs[x:x+4])

print(inputs[0])
