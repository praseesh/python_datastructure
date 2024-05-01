def shift_bits_left(num):
    num_ones = bin(num).count('1')
    new_num = (1 << num_ones) - 1  
    new_num <<= (8 - num_ones)  
    return new_num

num = 0b01010110
result = shift_bits_left(num)
print(bin(result))
