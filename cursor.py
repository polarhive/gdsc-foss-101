import time
import subprocess
import os

ascii_output = ""
pause = 0.1

def clear_screen():
    if os.name == 'posix':  # Unix-like OS
        subprocess.call('clear', shell=True)
    elif os.name == 'nt':  # Windows
        subprocess.call('cls', shell=True)

# Binary string to be converted
binary_string = "0110111001100101011101100110010101110010001000000110011101101111011011100110111001100001001000000110011101101001011101100110010100100000011110010110111101110101001000000111010101110000"

# Loop over the binary string in chunks of 8 bits (1 byte)
for i in range(0, len(binary_string), 8):
    byte = binary_string[i:i+8]
    
    clear_screen()
    cursor_position = " " * i + "^"  # Adjust the cursor position based on current index
    print(f"Binary String:\n{binary_string}\n{cursor_position}")
    print(f"Processing byte: {byte}")  # Extract 8 bits
    
    # binary byte to a decimal value
    decimal_value = int(byte, 2)
    print(f"Decimal value: {decimal_value}")
    
    # decimal value to the corresponding ASCII character
    ascii_char = chr(decimal_value)
    time.sleep(pause)
    print(f"ASCII character: {ascii_char}")
    
    ascii_output += ascii_char
    print(f"Current ASCII Output: {ascii_output}\n")
    
    time.sleep(pause)

