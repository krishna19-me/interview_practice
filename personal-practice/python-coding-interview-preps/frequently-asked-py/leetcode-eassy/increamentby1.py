def incrementby_one(l):
    v="".join([str(i) for i in l])
    out=[ int(i) for i in str(int(v)+1)]
    print(out)
incrementby_one([9])