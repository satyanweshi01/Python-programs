# 3. Define a recursive function to calculate factorial value of a number.
num = int(input("Enter the number: "))

def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)
f = factorial(num)
print(f)