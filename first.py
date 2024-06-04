def sumOfThree(nums: list) -> float:
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

if __name__ == "__main__":
    # nums: list = [input("1:"),input("2:"),input("3:")]
    # print(sumOfThree(nums))

    print(applesInBox("1.5", "1"))

