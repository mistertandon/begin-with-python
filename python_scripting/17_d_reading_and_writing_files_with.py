with open('./17_b_read_file.txt', 'r') as file_read:
    file_data = file_read.read()
"""
Display file content.
"""
print(file_data)
file_read.close()
