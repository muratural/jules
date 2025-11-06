import sys
import math

def calculate_circle_area(radius):
    """Calculates the area of a circle."""
    return math.pi * radius**2

if __name__ == "__main__":
    while True:
        try:
            radius_str = input("Enter the radius of the circle: ")
            r = float(radius_str)
            if r < 0:
                print("Error: Radius cannot be negative.")
                continue
            area = calculate_circle_area(r)
            print(f"The area of a circle with radius {r} is: {area:.4f}")
            break
        except ValueError:
            print("Error: Please enter a valid number for the radius.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break
