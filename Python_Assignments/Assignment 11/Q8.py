for row in range(10):
    if row % 2 == 0:
        # Left to Right
        start = row * 10 + 1
        end = start + 10
        for num in range(start, end):
            print(f"{num:3}", end=" ")
    else:
        # Right to Left
        start = (row + 1) * 10
        end = row * 10
        for num in range(start, end, -1):
            print(f"{num:3}", end=" ")

    print()
