class BottomUpMergeSort:
    from copy import deepcopy 
    
    def __init__(self, lst):
        self.lst = lst
        self.tmp_lst = []
        
    def flatten_nested_lists(self, nested_list):
        return [item for sublist in nested_list for item in sublist]

    def merge(self, left_lst, right_lst):
        # 리스트의 원소의 수가 1개 라면, 즉 리스트로 이루어져있지 않음
        if len(left_lst) == 1 and len(right_lst) == 1:
            if left_lst[0] > right_lst[0]:
                return right_lst + left_lst
            elif left_lst[0] < right_lst[0]:
                return left_lst + right_lst

        # 리스트 요소의 수가 1보다 크다면
        # 크기 비교하고 정렬 후 반환 
        checkpoint = True
        new_lst = []      
        while checkpoint:
            # 두 리스트에서 각 요소를 비교하고 정렬함
            if left_lst[0] >= right_lst [0]:
                new_lst.append(left_lst)
                left_lst.pop(0)
            elif left_lst[0] < right_lst [0]:
                new_lst.append(right_lst)
                right_lst.pop(0)
            
            # 리스트의 길이가 요소가 0이면 다른 하나의 리스트를 new_lst에 더함
            if len(left_lst) == 0:
                return new_lst + right_lst
            elif len(right_lst) == 0:
                return new_lst + left_lst
            
    def merge_sort(self):
        if len(self.lst) > 2: # 요소가 2보다 작을 경우 pass
            i = 0
            # print(len(self.lst))
            # print(self.lst[2*i])

            while len(self.lst) != (2*i):
                # 리스트 
                left_lst = [self.lst[2*i]]
                right_lst = [self.lst[2*i+1]] if i + 1 < len(self.lst) else []
                if all(isinstance(row, list) for row in left_lst):
                    
                    self.tmp_lst.append(self.merge(left_lst, right_lst))
                i += 1
            
            # 리스트를 복사
            # self.lst = [self.flatten_nested_lists(self.tmp_lst)]
            self.lst = list(self.tmp_lst)
            # 리스트를 초기화함
            self.tmp_lst = []
        
        if len(self.lst) != 1:
            self.merge_sort()
            
        # 리스트 반환
        return self.lst
    
data = [8,1,7,3,9,2,4,5]
sorter = BottomUpMergeSort(data)
print(sorter.merge_sort())