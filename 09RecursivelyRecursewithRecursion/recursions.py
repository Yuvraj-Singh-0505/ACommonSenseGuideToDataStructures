n = int(input("Enter how many terms of Fibonacci series you want: "))
a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
