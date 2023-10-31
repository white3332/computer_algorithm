def highlight_2d_list_elements(arr, highlight_indices):
    # 주어진 highlight_indices 리스트를 정렬합니다.
    sorted_indices = sorted(highlight_indices, key=lambda index: (index[0], index[1]))  

    i = 0
    new_list = []

    # 배열을 반복하면서 각 요소를 새로운 리스트에 추가합니다.
    for row_index, row in enumerate(arr):
        for col_index, item in enumerate(row):
            # 현재 위치가 정렬된 위치와 일치하는 경우, 해당 요소를 1로 표시하고 새로운 리스트에 추가합니다.
            if (i < len(sorted_indices)) and [row_index, col_index] == sorted_indices[i]:
                new_list.append([item, 1])
                i += 1
            else:
                # 일치하지 않는 경우, 해당 요소를 0으로 표시합니다.
                new_list.append([item, 0])

    col = 0

    # 새로운 리스트를 출력하면서, 1인 요소는 빨간색으로 표시하고 나머지는 원래 색으로 표시합니다.
    for element in new_list:
        if element[1] != 0:
            col += 1
            print("\033[91m" + str(element[0]) + "\033[0m", end="  ")  # 빨간색으로 설정 후 리셋
        else:
            col += 1
            print(str(element[0]), end="  ")

        # 한 행의 출력이 끝났을 때 줄 바꿈을 수행합니다.
        if col == len(arr[0]):
            col = 0
            print()

my_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 특정 위치를 빨간색으로 표시하여 출력합니다.
highlight_2d_list_elements(my_2d_array, [[1, 2], [2, 1], [1, 1], [0, 0], [0, 1]])  # (1, 1) 위치의 요소를 빨간색으로 표시
