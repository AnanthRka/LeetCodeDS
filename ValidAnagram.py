def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}

    for i in s:
        s_dict[i] = s_dict.get(i,0) + 1
    
    for i in t:
        t_dict[i] = t_dict.get(i,0) + 1

    for i in s_dict:
        if i not in t_dict or s_dict[i] != t_dict[i]:
            return False
    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))