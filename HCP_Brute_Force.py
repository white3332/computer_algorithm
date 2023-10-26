from copy import deepcopy
from itertools import permutations
import string

# 그래프를 인접 행렬로 표현
graph = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0]]





def generate_labels(count):
    labels = []
    for i in range(count):
        letter1 = string.ascii_uppercase[i % 26]  # 첫 번째 글자 (A, B, C, ...)
        label = letter1
        if len(labels) > 26:
            letter2 = string.ascii_uppercase[i // 26]  # 두 번째 글자 (A부터 Z까지 순환)
            label = letter2 + letter1
        labels.append(label)
    return labels

def find_hamiltonian_cycle(graph):
    vertices = generate_labels(len(graph))
    connect = []
    ret = []
    
    for i in range(len(graph)): # 간선을 찾음
        for j, value in enumerate(graph[i][i:]):
            if value == 1:
                connect.append([vertices[i], vertices[i+j]])
                
    copy_connect = deepcopy(connect)
    h_path = []
    h_path_vertices = []
    # 가능한 모든 순열을 생성
    edge = range(len(copy_connect))
    for path in permutations(edge):
        for index in path[0:len(vertices)+1]:
            # 맨 처음 반복에서는 if 문 true / 전에 연결된 정점과 연결되어 있는지 / 이미 지나간 정점은 다시 지나가지 않도록 함
            if (len(h_path) == 0) or (copy_connect[index][0] == h_path[len(h_path)-1][1]) and (copy_connect[index][1] not in h_path_vertices):
                h_path.append(list(copy_connect[index]))
                
                copy_connect[index][0] = 0
                copy_connect[index][1] = 0
                h_path_vertices.append(h_path[len(h_path)-1][0])
        
            # 맨 처음 반복에서는 if 문 true / 전에 연결된 정점과 연결되어 있는지 / 이미 지나간 정점은 다시 지나가지 않도록 함
            if (len(h_path) == 0) or (copy_connect[index][1] == h_path[len(h_path)-1][1]) and ((copy_connect[index][0] not in h_path_vertices) or ((copy_connect[index][0] == h_path_vertices[0]) and (len(h_path) == (len(vertices)-1)))):
                reversed_item = list(copy_connect[index])  # copy_connect[index]를 복사한 후
                reversed_item.reverse()  # 리스트를 뒤집고
                h_path.append(reversed_item)  # 뒤집힌 리스트를 h_path에 추가
                
                copy_connect[index][0] = 0
                copy_connect[index][1] = 0
                h_path_vertices.append(h_path[len(h_path)-1][0])
                    
                         
        # 경로를 찾음
        if len(h_path) == len(vertices):
            if h_path_vertices not in ret:
                ret.append(h_path_vertices)
                # print(f"경로 {h_path_vertices}")
                
        # 경로를 찾지 못해 다시 찾음, 리스트 초기화
        copy_connect = deepcopy(connect)
        h_path = []
        h_path_vertices = []
        reversed_item = []
        
    return ret

hamiltonian_cycle = find_hamiltonian_cycle(graph)
print(hamiltonian_cycle)

