import numpy as np
import pandas as pd
from copy import deepcopy
cost_matrix = pd.DataFrame(  [[7, 2, 9, 4],
                              [1, 3, 7, 4],
                              [1, 8, 9, 7],
                              [9, 6, 6, 5]])
cost_matrix = pd.DataFrame([[108, 125, 150],
                            [150, 135, 175],
                            [122, 148, 250]])

def Hungarian_Algorithm_step12 (cost_matrix):
    # axis=0는 열을 따라 작업하고, axis=1은 행을 따라 작업함
    # 행별 최소값 구한 후 빼줌
    row_min = cost_matrix.min(axis=1)
    cost_matrix = cost_matrix.sub(row_min, axis=0)

    # 열별 최소값 구한 후 빼줌
    column_min = cost_matrix.min(axis=0)
    cost_matrix = cost_matrix.sub(column_min, axis=1)
    
    return cost_matrix.values.tolist()  


def Hungarian_Algorithm_step3 (cost_matrix):
    cost_matrix = pd.DataFrame(cost_matrix)
    # 행렬의 마지막에 행과 열을 하나 씩 추가
    cost_matrix['CountColumn'] = 0
    cost_matrix.loc['CountRow'] = 0
    
    # 각 행과 열의 0의 개수를 구함
    cost_matrix['CountColumn'] = (cost_matrix.iloc[:-1,:-1] == 0).sum(axis=1).astype(int)
    cost_matrix.loc['CountRow'] = (cost_matrix.iloc[:-1,:-1] == 0).sum(axis=0).astype(int)
    cost_matrix.at['CountRow','CountColumn']=0
    cost_matrix = cost_matrix.astype(int)
    
    # 0을 가장 많이 포함하는 행 또는 열을 최소 개수 찾음
    row_max = (cost_matrix['CountColumn'] == cost_matrix['CountColumn'].max(axis=0))
    column_max = (cost_matrix.loc['CountRow'] == cost_matrix.loc['CountRow'].max(axis=0))


    step5_row_max = row_max.values.tolist() 
    step5_column_max = column_max.values.tolist() 
    
    return step5_row_max.index(True), step5_column_max.index(True)


def Hungarian_Algorithm_step4 (cost_matrix, row_matrix_step3, column_matrix_step3):
    cost_matrix_copy = deepcopy(cost_matrix)
    
    for idx_r, row in enumerate(cost_matrix_copy):
        if idx_r == row_matrix_step3:
            del cost_matrix_copy[row_matrix_step3]
            continue
        
        for idx_c, column in enumerate(row):
            if idx_c == column_matrix_step3:
                del cost_matrix_copy[idx_r][idx_c]
                continue

    return cost_matrix_copy
    
def Hungarian_Algorithm_step5(cost_matrix_step2,cost_matrix_step4,row_matrix_step3, column_matrix_step3):
    # 가장 작은 값, cost_matrix_step2을 덮어지지 않는 행에 최솟값을 빼줌
    cost_matrix = pd.DataFrame(cost_matrix_step4)
    min_cost = min(cost_matrix.min().values.tolist())
    New_cost_matrix = pd.DataFrame(cost_matrix_step2)
    New_cost_matrix = New_cost_matrix.sub(min_cost)
    
    cost_matrix = New_cost_matrix.values.tolist()
    
    # 제외할 행 및 열의 인덱스
    exclude_row_index = row_matrix_step3
    exclude_column_index = column_matrix_step3
     
    # 행 및 열을 제외하고 모든 값에 diff_value을 더합니다.
    diff_value = -min_cost
    result_matrix = []
    for row_index, row in enumerate(cost_matrix):
        new_row = []
        if row_index == exclude_row_index:
            result_matrix.append(row)
        elif row_index != exclude_row_index:
            for col_index, value in enumerate(row):
                if col_index == exclude_column_index:
                    new_row.append(value)
                elif col_index != exclude_column_index:
                    new_row.append(value + diff_value)
            result_matrix.append(new_row)
    result_matrix[row_matrix_step3][column_matrix_step3] =- diff_value

    return result_matrix


def Hungarian_Algorithm_step6(cost_matrix_step5):
    # 가능한 조합을 저장할 리스트
    possible_combinations = []

    # 가능한 조합을 찾기 위한 반복
    for i in range(len(cost_matrix_step5)):
        for j in range(len(cost_matrix_step5)):
            if cost_matrix_step5[i][j] == 0:
                possible_combinations.append([i, j])

    unique_value = None
    result = []
    copy_possible_combinations = deepcopy(possible_combinations)
    # 가능한 조합을 검사하고 유일한 값을 찾음
    for i in range(len(possible_combinations)):
        try:
            row_ = True
            col_ = True
            temp = possible_combinations[i][0]
            for item in possible_combinations:
                if item[0] == temp:
                    row_ = False
                    break
            
            temp = possible_combinations[i][1]
            for item in possible_combinations:
                if item[0] == temp:
                    col_ = False
                    break
                
            
            if row_ == True or col_ == True:
                print("모든 행과 열에서 하나의 0을 가지는 조합을 찾을 수 없음\n 최적 조합을 찾을 수 없음")
            else:
                result.append(item)
                possible_combinations.remove(item)
        except:
            pass




'''    print(count_item)
        if count_item == 
            unique_value = item
            result.append(item)
            possible_combinations.remove(item)
            break
        

        if (1 for item in possible_combinations if item[1] == 1):
            unique_value = item
            result.append(item)
            possible_combinations.remove(item)
            break
    if unique_value is None:
        print("모든 행과 열에서 하나의 0을 가지는 조합을 찾을 수 없음\n 최적 조합을 찾을 수 없음")
    else:
        print("찾은 최적 조합:", result)'''


cost_matrix_step2 = Hungarian_Algorithm_step12(cost_matrix)
row_matrix_step3, column_matrix_step3 = Hungarian_Algorithm_step3(cost_matrix_step2)
cost_matrix_step4 = Hungarian_Algorithm_step4 (cost_matrix_step2, row_matrix_step3, column_matrix_step3)
cost_matrix_step5 = Hungarian_Algorithm_step5(cost_matrix_step2,cost_matrix_step4,row_matrix_step3, column_matrix_step3)
cost_matrix_step6 = Hungarian_Algorithm_step6(cost_matrix_step5)