import numpy as np
import pandas as pd
from copy import deepcopy

def find_conbinations(possible_combinations):
    # 가능한 조합을 검사하고 유일한 값을 찾음
    for i in possible_combinations:
        row_has_zero = True
        col_has_zero = True
        
        # 같은 행에 0이 존재하는지 체크, 있으면 break
        for item in possible_combinations:
            if i == item: 
                pass
            else:
                if i[0] == item[0]:
                    row_has_zero = True
                    break
                else:
                    row_has_zero = False
            
        # 같은 열에 0이 존재하는지 체크, 있으면 break
        for item in possible_combinations:
            if i == item: 
                pass
            else:
                if i[1] == item[1]:
                    col_has_zero = True
                    break
                else:
                    col_has_zero = False
                    
        if row_has_zero == False or col_has_zero == False:
            break
        
    return row_has_zero, col_has_zero, i

def sub_matrix(cost_matrix):
    # 행과 열을 따라 최솟값을 찾아 해당 값을 행 또는 열의 모든 요소에서 빼줍니다.
    row_min = cost_matrix.min(axis=1)
    cost_matrix = cost_matrix.sub(row_min, axis=0)

    column_min = cost_matrix.min(axis=0)
    cost_matrix = cost_matrix.sub(column_min, axis=1)

    return cost_matrix.values.tolist()

def initialize_assignment_matrix(cost_matrix):
    # 비용 행렬을 데이터프레임으로 변환합니다.
    cost_matrix = pd.DataFrame(cost_matrix)

    # 행렬의 마지막 행과 열에 행 및 열 개수를 나타내는 카운터 열을 추가합니다.
    cost_matrix['CountColumn'] = 0
    cost_matrix.loc['CountRow'] = 0

    # 각 행과 열의 0의 개수를 계산하여 카운터 열에 저장하고 데이터 유형을 정수로 변환합니다.
    cost_matrix['CountColumn'] = (cost_matrix.iloc[:-1, :-1] == 0).sum(axis=1).astype(int)
    cost_matrix.loc['CountRow'] = (cost_matrix.iloc[:-1, :-1] == 0).sum(axis=0).astype(int)
    cost_matrix.at['CountRow', 'CountColumn'] = 0
    cost_matrix = cost_matrix.astype(int)

    # 0을 가장 많이 포함하는 행과 열을 최소로 설정하여 반환합니다.
    row_max = (cost_matrix['CountColumn'] == cost_matrix['CountColumn'].max(axis=0))
    column_max = (cost_matrix.loc['CountRow'] == cost_matrix.loc['CountRow'].max(axis=0))

    step5_row_max = row_max.values.tolist()
    step5_column_max = column_max.values.tolist()

    return step5_row_max.index(True), step5_column_max.index(True)

def remove_row_and_column(cost_matrix, row_to_remove, column_to_remove):
    # 입력된 비용 행렬의 복사본을 만듭니다.
    cost_matrix_copy = deepcopy(cost_matrix)

    # 삭제한 행을 추적하는 변수를 초기화합니다.
    removed_row = 0

    # 비용 행렬의 각 행에 대해 반복합니다.
    for idx_r, row in enumerate(cost_matrix):
        if idx_r == row_to_remove:
            # 선택된 행을 삭제하기 위해 복사본에서 해당 행을 제거합니다.
            del cost_matrix_copy[row_to_remove]

            # 행을 삭제했으므로 removed_row를 1로 설정하여 인덱스 조정에 사용합니다.
            removed_row = 1
            continue

        # 비용 행렬의 각 열에 대해 반복합니다.
        for idx_c, column in enumerate(row):
            if idx_c == column_to_remove:
                # 선택된 열을 삭제하기 위해 복사본에서 해당 열을 제거합니다.
                del cost_matrix_copy[idx_r - removed_row][idx_c]

    # 수정된 비용 행렬을 반환합니다.
    return cost_matrix_copy

def adjust_cost_matrix(cost_matrix_step2, cost_matrix_step4, row_matrix_step3, column_matrix_step3):
    # 제외할 행 및 열의 인덱스
    excluded_row_index = row_matrix_step3
    excluded_column_index = column_matrix_step3
    
    # 부분 행렬에서 가장 작은 값을 찾습니다.
    partial_cost_matrix = pd.DataFrame(cost_matrix_step4)
    min_cost = min(partial_cost_matrix.min().values.tolist())
    
    # 새로운 비용 행렬을 생성하여 업데이트합니다.
    new_cost_matrix = pd.DataFrame(cost_matrix_step2)
    
    # 제외된 행을 제외하고 최솟값을 빼줍니다.
    for i in range(len(cost_matrix_step2)):
        if excluded_row_index != i:
            new_cost_matrix.iloc[i] = new_cost_matrix.iloc[i].sub(min_cost)
    
    # 제외된 열에 최솟값을 더해줍니다.
    for i in range(len(cost_matrix_step2)):
        if excluded_column_index == i:
            new_cost_matrix.iloc[:, i] = new_cost_matrix.iloc[:, i].add(min_cost)
    
    result_matrix = new_cost_matrix.values.tolist()
    
    return result_matrix

def find_unique_combinations_with_zeros(cost_matrix_step5):
    # 가능한 조합을 저장할 리스트
    possible_combinations = []

    # 가능한 조합을 찾기 위한 반복(0이 들어간 조합을 모두 찾음)
    for i in range(len(cost_matrix_step5)):
        for j in range(len(cost_matrix_step5)):
            if cost_matrix_step5[i][j] == 0:
                possible_combinations.append([i, j])

    result = []
    while len(cost_matrix) != len(result):
                    
        row_has_zero, col_has_zero, item = find_conbinations(possible_combinations)
        if 1 == len(possible_combinations):
            result.append(item)
            break
            
        if row_has_zero == True and col_has_zero == True:
            print("모든 행과 열에서 하나의 0을 가지는 조합을 찾을 수 없음\n 최적 조합을 찾을 수 없음")
        elif row_has_zero == False or col_has_zero == False:
            result.append(item)
            possible_combinations.remove(item)
            for i in possible_combinations:
                if i[0] == item[0]:
                    possible_combinations.remove(i)
                    continue
                if i[1] == item[1]:
                    possible_combinations.remove(i)
    return result

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


# 주어진 cost_matrix에서 최적 조합을 찾고 출력합니다.
cost_matrix = pd.DataFrame([[108, 125, 150],
                            [150, 135, 175],
                            [122, 148, 250]])
cost_matrix = pd.DataFrame([[10, 25, 15, 20],
                            [15, 30, 5, 15],
                            [35, 20, 12, 24],
                            [17, 25, 24, 20]])

cost_matrix_step2 = sub_matrix(cost_matrix)
row_matrix_step3, column_matrix_step3 = initialize_assignment_matrix(cost_matrix_step2)
cost_matrix_step4 = remove_row_and_column(cost_matrix_step2, row_matrix_step3, column_matrix_step3)
cost_matrix_step5 = adjust_cost_matrix(cost_matrix_step2, cost_matrix_step4, row_matrix_step3, column_matrix_step3)
cost_matrix_step6 = find_unique_combinations_with_zeros(cost_matrix_step5)
print(cost_matrix_step6)

# 최적 조합을 하이라이트하여 출력
highlight_2d_list_elements(cost_matrix.values.tolist(), cost_matrix_step6)