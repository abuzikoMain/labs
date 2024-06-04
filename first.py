a: str = input()
b: str = input()
c: str = input()

sum: int = 0

for each in [a, b, c]:
    try:
        each = int(each)
        sum += each
    except Exception as e:
        print(f"Exc {e}")

print(sum)