print("Read Operation\n")
file_read = open('./17_b_read_file.txt', 'r')
file_data = file_read.read()
"""
Display file content.
"""
print(file_data)
file_read.close()

print("\nWrite Operation\n")
file_write = open('./17_c_write_file.txt', 'r+')
file_write.write('Hi,content of 17_c_write_file.txt')
file_data = file_write.read()
"""
Display file content.
"""
print(file_data)
file_write.close()