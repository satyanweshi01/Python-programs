# 7. Define filter() to check the ages in the list which are greater than 18.

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

a = eval(input("Enter list: "))
b = list(filter(is_adult,a))
print(b)