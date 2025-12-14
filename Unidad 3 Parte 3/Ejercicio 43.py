num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

start = min(num1, num2)
end = max(num1, num2)

print(f"Los números pares entre {start} y {end} son:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
