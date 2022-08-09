def firstUniqChar(s: str) -> int:

    s_dict = {}
    
    for i in s:
        s_dict[i] = s_dict.get(i,0) + 1
    
    for i in s_dict:
        if s_dict[i] == 1:
            return s.index(i)
    return -1

print(firstUniqChar( "leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))