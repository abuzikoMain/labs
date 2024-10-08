import math

def sumOfThree(nums: list[str]) -> float:
    sum: float = 0
    for each in nums:
        try:
            each = float(each)
            sum += each
        except Exception as e:
            print(f"Exc: {e}")
    return sum

def AreaOfRightTriangle(base: str, height: str) -> float:
    area: float = 1
    try:
        for each in [base, height]:
            each = float(each)
            area *= each
            if each <= 0:
                area = 0

        area *=0.5 

    except Exception as e:
        area = 0
        print(f"Exc: {e}")

    return area

def applesInBox(x: str, y:str) -> tuple[int, int]:
    foreach: float = 0
    remain: float = 0
    
    try:
        x = int(x)
        y = int(y)

        remain = x % y
        foreach = x // y
    except Exception as e:
        print(f"Exc: {e}")

    return foreach, remain

def clock(m: str) -> str:
    hours:int = 0
    minutes: int = 0
    try:
        m = int(m)

        while m > 60:
            m -= 60
            hours += 1

            hours = 0 if hours == 24 else hours

        minutes = m
    except Exception as e:
        print(f"Exc: {e}")

    return f"{hours} {minutes}"

def helloWorld(string: str) -> str:
    return f"Hello, {string}!"

def nextAndPast(number: str) -> str:
    output: str
    try:
        number = float(number)
        past_num = number - 1
        next_num = number + 1
    except Exception as e:
        print(f"exc {e}")
    
    output = f"The next number for the number {number} is {next_num}\n The previous number for the number {number} is {past_num}"

    return output

def parts(groups: list[str]) -> int:
    count_pc: int = 0
    if not isinstance(groups, list):
        return 0
    for each in groups:
        try:
            each = int(each)
            count_pc += math.ceil(each / 2)
        except Exception as e:
            print(f"exc: {e}. Not valid {each}")

    return count_pc

def lace_length(a, b, L, N):
    a = int(input())
    b = int(input())
    L = int(input())
    N = int(input())
    print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)

if __name__ == "__main__":
    ...
