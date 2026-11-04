a = 10
b = 10

print(f"a : {id(a)}")
print(f"b : {id(b)}")

print(a is b)

c = 1000000000000000
d = 1000000000000000

print(f"c : {id(c)}")
print(f"d : {id(d)}")

print(c is d)

# I think python caches object cause the used int object have same object id