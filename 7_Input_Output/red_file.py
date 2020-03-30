my_file = open("C:\\Desarrollo\\PythonScripts\\7_Input_Output\\data.txt")
for d in my_file:
    print(d, end="")

my_file2 = open("C:\\Desarrollo\\PythonScripts\\7_Input_Output\\song.txt")
for d in my_file2:
    print(d, end="")

#A good practice is using the with keyword to prevent open and close the open functionality

with open("C:\\Desarrollo\\PythonScripts\\7_Input_Output\\song.txt") as f:
    read_data = f.read()
    for line in read_data:
        print(line.upper(), end="")

#For write in a file you can use write, remember to load the file with write privileges

my_file_w = open("C:\\Desarrollo\\PythonScripts\\7_Input_Output\\data.txt","w")
my_file_w.write("THIS TEXT IS FROM SCRIPT CODE")





