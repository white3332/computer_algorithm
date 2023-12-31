import string
from copy import deepcopy

# 정점 레이블 초기화
vertex = []
# 주어진 인접 행렬
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

# 정점 레이블 생성 함수
def generate_vertex(count):
    vertex = []
    for i in range(count):
        letter1 = string.ascii_uppercase[i % 26]
        label = letter1
        if len(vertex) > 26:
            letter2 = string.ascii_uppercase[i // 26]
            label = letter2 + letter1
        vertex.append(label)
    return vertex

# DFS 함수
def DFS(graph):
    # 정점 레이블 생성
    vertices = generate_vertex(len(graph))
    # 연결된 간선 저장
    connect = []
    # 스택 초기화
    stack = []
    # 방문한 정점 저장
    ret = []

    # 간선 정보 수집
    for i in range(len(graph)):
        for j, value in enumerate(graph[i][i:]):
            if value == 1:
                connect.append([vertices[i], vertices[i+j]])
    # 연결 정보 복사
    copy_connect = deepcopy(connect)

    # 시작 정점 설정
    out_vertex = copy_connect[0][0]
    last_out_vertex = None

    # 스택이 비어 있지 않거나 모든 정점을 방문할 때까지 반복
    while stack or len(ret) < len(vertices):
        # 현재 정점을 아직 방문하지 않았다면 추가
        if out_vertex not in ret:
            ret.append(out_vertex)

        # 인접 정점 중 스택과 방문한 정점 목록에 없는 정점을 스택에 추가
        for edge in reversed(copy_connect):
            if edge[0] == out_vertex and edge[1] not in stack and edge[1] not in ret:
                stack.append(edge[1])
            if edge[1] == out_vertex and edge[0] not in stack and edge[0] not in ret:
                stack.append(edge[0])

        # 스택이 비어있지 않다면 스택에서 정점을 꺼내어 다음 방문 정점으로 설정
        if stack:
            last_out_vertex = out_vertex
            out_vertex = stack.pop()
            try:
                copy_connect.remove([last_out_vertex, out_vertex])
            except:
                try:
                    copy_connect.remove([out_vertex, last_out_vertex])
                except:
                    pass

    return ret

# DFS 수행 및 결과 출력
print(DFS(adjMat))