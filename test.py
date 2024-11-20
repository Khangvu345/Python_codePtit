def is_non_decreasing(number):
    """
    Kiểm tra liệu số nguyên dương `number` có phải là số không giảm hay không.
    """
    str_num = str(number)
    for i in range(len(str_num) - 1):
        if str_num[i] > str_num[i + 1]:
            return False
    return True


if __name__ == "__main__":
    # Đọc số bộ test
    test_cases = int(input().strip())

    # Lặp qua từng bộ test và kiểm tra
    for _ in range(test_cases):
        number = input().strip()
        if is_non_decreasing(number):
            print("YES")
        else:
            print("NO")
