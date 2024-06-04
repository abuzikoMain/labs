def sumOfThree(nums: list):
    sum: float = 0
    for each in nums:
        try:
            each = float(each)
            sum += each
        except Exception as e:
            print(f"Exc {e}")
    return sum

if __name__ == "__main__":
    nums: list = [input("1:"),input("2:"),input("3:")]
    print(sumOfThree(nums))


print(sum)