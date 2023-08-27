# Input binary number as a list of integers
a = list(map(int, input("Enter your binary number: ")))

# Input divisor (used for CRC) as a list of integers
divisor = list(map(int, input("Enter your divisor: ")))

# Length of the divisor
b = len(divisor)

# Validate input binary number
for bit in a:
    if bit != 0 and bit != 1:
        print("Enter valid binary number")
        a = list(map(int, input("Enter your binary number: ")))

# Extend the binary number with zeros to prepare for CRC
a.extend([0] * (b - 1))

# Perform CRC calculation
for i in range(len(a) - b + 1):
    if a[i] == 1:
        for j in range(b):
            a[i + j] ^= divisor[j]  # XOR operation

# Get the remainder (CRC result)
r = a[-(b - 1):]

# Check if remainder is all zeros
if all(bit == 0 for bit in r):
    print("No errors (not corrupted)")
else:
    print("Error detected (corrupted)")
