def tower(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower(n-1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower(n-1, auxiliary, source, destination)


# Main program
n = 3

print("Tower of Hanoi Solution:")

tower(n, 'A', 'B', 'C')