def solution(arr, queries):
    for qu in queries:
        arr[qu[0]], arr[qu[1]] = arr[qu[1]], arr[qu[0]]
    return arr