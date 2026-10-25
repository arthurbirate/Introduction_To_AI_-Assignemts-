from fastapi import FastAPI

app = FastAPI()


@app.post("/add")
def add(a,b):

    # lstrip() removes any - sign before the number to check if it is a digit or not 
    if a.lstrip("-").isdigit() and b.lstrip("-").isdigit():
        sum = int(a) + int(b)
        return {"sum":sum}

    else :
        return  {"Please use real numbers 0 - 10 negatives are allowed"}


