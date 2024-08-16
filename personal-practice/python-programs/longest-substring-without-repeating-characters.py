def longestSubstring(s : str):
    longest = 0
    start = 0 
    end = 1
    
    while end <= len(s):
        if len(s[start:end]) == len(set(s[start:end])):
            longest = max(longest, len(s[start:end]))
            end+=1
        else:
            start+=1
    return longest

strings = ["abccdcb" ,"aaaaaa" ,"pwwkew"]
for s in strings:
    print(longestSubstring(s))