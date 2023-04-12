for i in range(1, 8):
    print("#", end="")
    for j in range(0, i):
        if j == i - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
