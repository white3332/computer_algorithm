def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 테스트
import random as rd
create_range = rd.randint(1, 1000)
arr = []
for i in range(create_range):
    arr.append(rd.randint(-200, 200))
    
import numpy as np
arr = np.array(arr) + np.array(200)
radix_sort(arr)
arr = np.array(arr) - np.array(200)

print("정렬된 배열:", arr)
