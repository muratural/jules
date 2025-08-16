import sys

def calculate_averages(num1, num2, num3):
    """Calculates the arithmetic and geometric averages of three numbers."""
    # Calculate the arithmetic average
    arithmetic_avg = (num1 + num2 + num3) / 3

    # Calculate the geometric average
    product = num1 * num2 * num3
    if product < 0:
        # Complex numbers would be required, which is outside the scope.
        geometric_avg_str = "not defined for negative products"
    else:
        # Use abs() to handle potential floating point inaccuracies near zero
        geometric_avg = abs(product) ** (1/3)
        geometric_avg_str = f"{geometric_avg:.4f}"


    print(f"Numbers: {num1}, {num2}, {num3}")
    print(f"Arithmetic Mean: {arithmetic_avg:.4f}")
    print(f"Geometric Mean: {geometric_avg_str}")

if __name__ == "__main__":
    # The script name is sys.argv[0], so we expect 4 arguments total
    if len(sys.argv) != 4:
        print("Usage: python average_calculator.py <num1> <num2> <num3>")
        sys.exit(1)

    try:
        # Convert arguments to floats
        n1 = float(sys.argv[1])
        n2 = float(sys.argv[2])
        n3 = float(sys.argv[3])

        calculate_averages(n1, n2, n3)

    except ValueError:
        print("Error: All arguments must be valid numbers.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
