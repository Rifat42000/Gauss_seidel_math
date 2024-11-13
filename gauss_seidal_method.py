# Parameters
tolerance = 1e-5  # convergence tolerance
max_iterations = 1  # maximum number of iterations

# Initial guesses
x, y, z = 0, 0, 0

# Gauss-Seidel Iteration
for k in range(max_iterations):
    x_new = (1 / 6) * (24 - 5 * y + 8 * z)
    y_new = (1 / 8) * (10 - 3 * z)
    z_new = (1 / 4) * (11 - 10 * x_new - 3 * y_new)

    # Check for convergence
    if abs(x - x_new) < tolerance and abs(y - y_new) < tolerance and abs(z - z_new) < tolerance:
        break

    # Update values for the next iteration
    x, y, z = x_new, y_new, z_new

print(f"Solution after {k + 1} iterations:")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")
