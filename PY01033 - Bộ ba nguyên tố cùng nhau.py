from math import *

def bo_ba_nguyen_to_cung_nhau(L, R):
    danh_sach = []

    for a in range(L, R - 1):
        for b in range(a + 1, R):
            if gcd(a, b) == 1:
                for c in range(b + 1, R + 1):
                    if gcd(a, c) == 1 and gcd(b, c) == 1:
                        danh_sach.append((a, b, c))
    return danh_sach

L, R = map(int, input().split())
ket_qua = bo_ba_nguyen_to_cung_nhau(L, R)

for i in ket_qua:
    print(i)
