
# 행렬 요소의 수가 홀수개이면 오류



class BottomUpMergeSort:
    from copy import deepcopy 
    
    def __init__(self, lst):
        self.lst = lst
        self.tmp_lst = []
        
    def is_nested_array(self, arr):
        # 검사를 위한 임의의 요소를 추출
        sample_element = arr[0] if arr else None
        
        # 추출한 요소가 리스트인지 확인하여 2중 배열 여부 판단
        return isinstance(sample_element, list) if sample_element is not None else False


    def merge_nested_lists(self, nested_list):
        return [item for item in nested_list]

    def merge(self, left_lst, right_lst):
        # 리스트의 원소의 수가 1개 라면
        if self.is_nested_array(left_lst) != True and self.is_nested_array(right_lst) != True :
            if left_lst[0] > right_lst[0]:
                return right_lst + left_lst
            elif left_lst[0] < right_lst[0]:
                return left_lst + right_lst
            
        elif self.lst[-1] == right_lst [0]:
            # 리스트 요소의 수가 짝수 일때
            pass
        else:
            # 리스트 요소의 수가 1보다 크다면
            # 크기 비교하고 정렬 후 반환 
            checkpoint = True
            new_lst = []      
            while checkpoint:
                # 두 리스트에서 각 요소를 비교하고 정렬함
                if left_lst[0][0] >= right_lst [0][0]:
                    new_lst.append(right_lst[0][0])
                    right_lst[0].pop(0)
                elif left_lst[0][0] < right_lst [0][0]:
                    new_lst.append(left_lst[0][0])
                    left_lst[0].pop(0)
                
                # 리스트의 길이가 요소가 0이면 다른 하나의 리스트를 new_lst에 더함
                if len(left_lst[0]) == 0:
                    return new_lst + right_lst[0]
                elif len(right_lst[0]) == 0:
                    return new_lst + left_lst[0]
            
    def merge_sort(self):
        if len(self.lst) >= 2: 
            i = 0
            # 리스트의 요소가 짝수인가?
            isodd = ((len(self.lst) // 2) == 0)
            # 요소가 2보다 작을 경우 pass
            try:
                while len(self.lst) > (2*i):
                    left_lst = [self.lst[2*i]]
                    right_lst = [self.lst[2*i+1]]
                    self.tmp_lst.append(self.merge(left_lst, right_lst))
                    i += 1
            except:
                pass
            if isodd == True:
                # 리스트를 복사
                self.lst = list(self.tmp_lst)
                    # 리스트를 초기화함
                self.tmp_lst = []
                if len(self.lst) != 1:
                    self.merge_sort()
            else:
                # 데이터 요소의 수가 짝수일 경우 예외 처리
                self.lst = list(self.tmp_lst + [self.lst[-1]])
                # 리스트를 초기화함
                self.tmp_lst = []
                if len(self.lst) != 2:
                    self.merge_sort()
        # 리스트 반환
        return self.merge_nested_lists(self.lst[0])
    
data = [8,1,7,3,9,2,4,5]
sorter = BottomUpMergeSort(data)
print(sorter.merge_sort())