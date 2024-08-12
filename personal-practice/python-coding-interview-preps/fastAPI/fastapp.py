from fastapi import FastAPI
import json,uvicorn

app=FastAPI()

@app.get("/poly")
def findpolindrome():
    print("Inside polindrome check")
    return f"Inside polindrome check"

@app.get("/poly/{poliystring}")
def findpolindrome1(poliystring:str):
    return {"polindrome",poliystring==poliystring[::-1]}

@app.get("/helo/{multistring}")
def findpolindrome2(multistring:str):
    dic={}
    for string in multistring.split("-"):
        dic[string]=(string==string[::-1])
    print(dic)    
    return json.dumps(dic) 


if __name__=="__main__":
    uvicorn.run(app,port=8001)

# if __name__ == "__main__":
#     uvicorn.run("example:app", host="127.0.0.1", port=5000, reload=True)

