s = "abc"
t = "ahbgdc"

# print(all(s))
def is_subsequence(s,t):
    for i in s:
        if i not in t:
            return False
    return True

print(is_subsequence(s,t))