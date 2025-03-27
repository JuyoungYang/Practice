def solution(bin1, bin2):
    decimal_bin1 = int(bin1, 2)
    decimal_bin2 = int(bin2, 2)
    decimal_sum = decimal_bin1 + decimal_bin2
    binary_sum = bin(decimal_sum)[2:]  # "0b" 접두사 제거
    return binary_sum