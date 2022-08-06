def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:

    flat = []
    out = []

    for i in mat:
        for j in i:
            flat.append(j)
    
    if len(flat) != r *c:
        return mat
    else:
        for i in range(0,len(flat),c):
            out.append(flat[i:i+c])
    return out

print(matrixReshape([[1,2],[3,4]], 1,4))
print(matrixReshape([[1,2],[3,4]], 2,4))