string1 = "krishna"
string2 = "roshini"

print(set(string1) & set(string2))

# count ch in string

string1 = "aaabbbackbsjjj"

newset = set(string1)
print([(string1.count(ch), ch) for ch in newset if ch in string1])


students = [('David', 46), ('sam', 56), ('sagar', 90)]

print(max(students, key=lambda student: student[1]))
