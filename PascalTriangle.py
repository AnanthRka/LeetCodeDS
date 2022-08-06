def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    
    output = []

    for i in range(numRows):
        temp = [1]* (i+1)
        
        if i== 0 or i ==1:
            output.append(temp)
        else:
            for j in range(1,i):
                temp[j] = output[i-1][j-1] + output[i-1][j]
            output.append(temp)
    return output

for i in range(1,6):
    print(generate(i))
    print()