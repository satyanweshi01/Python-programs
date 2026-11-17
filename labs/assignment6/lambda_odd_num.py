# 6.Define lambda function to find out odd number within a sequence.

a = eval(input("Enter the sequence(like list): "))
# is_odd = lambda x:x%2 != 0

# print(is_odd(a[0]))

b = list(filter(lambda x:x%2 != 0,a))
print(b)