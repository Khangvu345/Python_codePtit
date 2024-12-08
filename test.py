def generate_even_palindromes(limit):
    even_digits = ['0', '2', '4', '6', '8']  # Chỉ sử dụng các chữ số chẵn
    result = []  # Danh sách các số thoả mãn

    max_len = len(str(limit))  # Số chữ số tối đa
    for length in range(2, max_len + 1, 2):  # Chỉ xét độ dài chẵn
        half_length = length // 2  # Nửa đầu của số thuận nghịch
        for half in product(even_digits, repeat=half_length):
            # Không cho phép số bắt đầu bằng 0
            if half[0] == '0':
                continue

            # Tạo nửa đầu và nửa sau
            first_half = ''.join(half)
            full_number = int(first_half + first_half[::-1])

            # Kiểm tra nếu số thoả mãn
            if full_number < limit:
                result.append(full_number)

    return result


if __name__ == "__main__":
    from itertools import product  # Dùng để sinh tổ hợp

    for _ in range(int(input())):
        n = int(input())  # Đọc giá trị n
        result = generate_even_palindromes(n)  # Gọi hàm sinh số thuận nghịch
        print(*result)  # In danh sách kết quả, cách nhau bởi khoảng trắng

