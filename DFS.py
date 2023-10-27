

import string
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

adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]
vertex = generate_labels(len(adjMat))

