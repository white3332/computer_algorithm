my_2d_array = [[1, 2], [2, 1], [1, 1], [0, 0], [0, 1]]

sorted_array = sorted(my_2d_array, key=lambda x: (x[0], x[1]))  # 두 번째 요소를 기준으로 오름차순 정렬, 그 다음 첫 번째 요소를 기준으로 정렬

for item in sorted_array:
    print(item)
