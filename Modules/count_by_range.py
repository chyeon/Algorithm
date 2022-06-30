# 값이 left_value ~ right_value 범위에 속하는 데이터 개수 반환
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_vaue)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
