sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

def maxWords(sentences):
    return max([len(s.split(" ")) for s in sentences])

print(maxWords(sentences))

