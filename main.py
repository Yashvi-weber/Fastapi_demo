from fastapi import FastAPI
from config import a,b

app = FastAPI()

@app.get("/sum")
def sum(a:int,b:int):
    return {"sum": a+b}



print(a)
print(b)
