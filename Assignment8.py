file_name='output.txt'
data1 = str(input("Enter text to write to the file:"))
#data1= Hello, Python!
file1 = open(file_name, 'w')
file1.write(data1)
file1.close()
print("Data Successfully written to " + file_name + '.')
print(("\n") *2)

data2 = str(input("Enter additional text to append:"))
#data2=Learning file handling in Python.
file1 = open(file_name, 'a')
file1.write('\n' + data2)
file1.close()
print("Data Successfully appended" + '.')
print(("\n") *2)

print("Final content of " + file_name + ':')
file1 = open(file_name,'r')
data3 = file1.read()
print(data3)

file1.close()