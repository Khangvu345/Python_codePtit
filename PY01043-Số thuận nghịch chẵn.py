from itertools import product

def kiem_tra_so_thuan_nghich_chan(n):
    length_max = len(str(n))
    even_digits= "02468"
    result = []

    for length_i in range(2, length_max+1, 2):
        for i in product(even_digits, repeat=length_i // 2):
            if i[0] == "0":
                continue
            full= int(''.join(i) + ''.join(i[::-1]) )
            if full < N:
                result.append(full)
    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(*kiem_tra_so_thuan_nghich_chan(N))