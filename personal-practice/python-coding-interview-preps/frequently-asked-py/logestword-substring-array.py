
def subarray(s,w):
    d={}
    for word in s:
        if w in word:
            d[len(word)]=word
    return max({k for k in d.keys()})
s=["CODGE","ODG","LODGES","SODG","dodge","mODJ","LODGESSSS"]
w="ODG"
print(subarray(s,w)) 