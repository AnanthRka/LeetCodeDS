def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    r = len(matrix)
    c = len(matrix[0])

    start = 0
    end = r*c -1

    while start <= end:
        mid = (start+end) //2
        num = matrix[mid//c][mid % c]
        if num ==target:
            return True
        elif num < target:
            start = mid +1
        else:
            end = mid -1
    return False

print(searchMatrix( [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))