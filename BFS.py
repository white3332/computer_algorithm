import string

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

# BFS 함수
def BFS(graph):
    vertices = generate_vertex(len(graph))
    queue = []  # 큐 초기화
    visited = [False] * len(graph)  # 방문한 정점을 추적하는 리스트
    ret = []  # 방문한 정점 순서를 저장할 리스트

    # 정점을 방문하는 함수
    def visit(v):
        ret.append(v)
        visited[vertices.index(v)] = True

    # 시작 정점 설정
    start_vertex = generate_vertex(1)[0]

    visit(start_vertex)  # 시작 정점 방문
    queue.append(start_vertex)  # 큐에 시작 정점 추가

    while queue:
        v = queue.pop(0)  # 큐에서 정점 추출 (먼저 들어온 것을 먼저 방문)
        v_index = vertices.index(v)
        for i, edge in enumerate(graph[v_index]):
            if edge == 1 and not visited[i]:
                visit(vertices[i])  # 연결된 정점 방문
                queue.append(vertices[i])  # 큐에 연결된 정점 추가

    return ret

# BFS 수행 및 결과 출력
print(BFS(adjMat))