# 4. Define a function to find prime numbers with in the range 10 to 30.

def is_prime(num):
    print(num)
    if num <2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def prime_find(start,stop,storage):
    for i in range(start,stop+1):
        if is_prime(i):
            storage.append(i)
s = []
start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))

prime_find(start,stop,s)
print(s)