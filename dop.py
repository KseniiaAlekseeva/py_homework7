def print_operation_table(operation, nr, nc):
    print('    ', end=' ')
    for j in range(1, nc+1):
        print(j, end=' ')
    print("\n")

    for i in range(1, nr+1):
        print(i, end='    ')
        for j in range(1, nc+1):
            print(operation(i, j), end=' ')
        print("\n")


print_operation_table(lambda x, y: x+y, 5, 9)
