file_name = "reading.txt"

file_path = f"../{file_name}"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist")