# where's the bytecode?
pyc_file_path = "__pycache__/helloworld.cpython-312.pyc"
with open(pyc_file_path, 'rb') as file:
    binary_data = file.read()

# convert the binary data to a string of 1s and 0s
print(''.join(format(byte, '08b') for byte in binary_data))

