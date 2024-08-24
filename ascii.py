import time

binary_string = "0110111001100101011101100110010101110010001000000110011101101111011011100110111001100001001000000110011101101001011101100110010100100000011110010110111101110101001000000111010101110000"

ascii_output = ""
pause = 0.2

# Loop over the binary string in chunks of 8 bits (1 byte)
for i in range(0, len(binary_string), 8):
    byte = binary_string[i:i+8]
    print(f"Processing byte: {byte}") # Extract 8 bits
    
    # Convert the binary byte to a decimal value
    decimal_value = int(byte, 2)
    print(f"Decimal value: {decimal_value}")
    
    # Convert the decimal value to the corresponding ASCII character
    ascii_char = chr(decimal_value)
    time.sleep(pause)
    print(f"ASCII character: {ascii_char}")
    
    
    # Print the current state of the ASCII output
    ascii_output += ascii_char
    print(f"Current ASCII Output: {ascii_output}\n")
