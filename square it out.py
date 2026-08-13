start, end = int(input("Start: ")), int(input("End: "))

squares = [x**2 for x in range(start, end + 1)]
even = [sq for sq in squares if sq % 2 == 0]
odd = [sq for sq in squares if sq % 2 != 0]

print(f"Squares: {squares}")
print(f"Even: {even}")
print(f"Odd: {odd}")
