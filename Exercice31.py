n = int(input("Please enter an integer n greater than 2: "))

U0 = 0
U1 = 1

print("The Fibonacci sequence up to", n, ":")
print(U1)

while U0 + U1 <= n:
    Un = U0 + U1
    print(Un)
    U0 = U1
    U1 = Un
