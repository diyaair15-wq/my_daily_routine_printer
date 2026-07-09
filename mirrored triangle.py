def mirror_triangle(n: int) -> None:
    """Print a right-aligned (mirrored) right-angle triangle of height n using '*' characters."""
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)



n = int(input("Enter the number of rows: "))
mirror_triangle(n)
    