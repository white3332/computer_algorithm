def is_nested_array(self, arr):
    # 검사를 위한 임의의 요소를 추출
    sample_element = arr[0] if arr else None
    
    # 추출한 요소가 리스트인지 확인하여 2중 배열 여부 판단
    return isinstance(sample_element, list) if sample_element is not None else False