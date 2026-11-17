# 5. Define lambda function to multiply 2 lists
a = eval(input("Enter the list 1: "))
b = eval(input("Enter the list 2: "))

c = list(map(lambda x : x[0]*x[1],zip(a,b))) # returns zip object(iterator of tuples)
print(c)