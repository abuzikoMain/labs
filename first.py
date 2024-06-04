def sumOfThree(nums: list):
    sum: float = 0
    for each in nums:
        try:
            each = float(each)
            sum += each
        except Exception as e:
            print(f"Exc: {e}")
    return sum


def AreaOfRightTriangle(base, height):
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

if __name__ == "__main__":
    # nums: list = [input("1:"),input("2:"),input("3:")]
    # print(sumOfThree(nums))

    print(AreaOfRightTriangle(input("base: "), input("height: ")))


print(sum)