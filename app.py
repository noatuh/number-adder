import sys

# Check if exactly two arguments are passed
if len(sys.argv) != 3:
    print("Error: Please enter exactly two numbers.")
else:
    try:
        # Convert arguments to floats and calculate the sum
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
