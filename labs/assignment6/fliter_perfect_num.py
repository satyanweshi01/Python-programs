# 8. Define filter to check perfect no in a sequence()

def is_perfect_num(age):
    sum = 0
    for i in range(1,age):
        if (age%i == 0):
            sum = sum+i
    if (age==sum):
        return True
    return False

a = eval(input("Enter list: "))
b = list(filter(is_perfect_num,a))
print(b)