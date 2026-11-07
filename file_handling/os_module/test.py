import os
# file detection
def write_content(file_path):
    with open(file_path,"w") as file:
        file.write("There is a brown fox")
    with open(file_path,"r") as file:
        content = file.read()
        print(content)

file_name = "text.txt"

file_path = f"../{file_name}"

if os.path.exists(file_path):
    print(f"{file_name} do exists")

    if os.path.isfile(file_path):
        print("This is a file")
    if not os.path.isdir(file_path):
        print("This is not a directory")

    write_content(file_path)

else:
    print(f"{file_name} do not exists")
    print(f"creating the file.....")

    write_content(file_path)
