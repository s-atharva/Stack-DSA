from typing import List


def nearest_greater_to_right(arr: List[int]) -> List[int]:
    v = []
    s = []
    for i in range(len(arr) - 1, -1, -1):
        if len(s) == 0:
            v.append(-1)
        elif len(s) and s[-1] > arr[i]:
            v.append(s[-1])
        else:
            while len(s) and s[-1] <= arr[i]:
                s.pop()
            if len(s) == 0:
                v.append(-1)
            else:
                v.append(s[-1])
        s.append(arr[i])
    return v[::-1]


arr = [1, 3, 2, 4]
print(nearest_greater_to_right(arr=arr))
