from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, yaakov"}


@app.get("/ping")
def ping():
    return {"status": "pong"}


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("users/admin")
def get_admin():
    return {"user_id": admin, type: "super_admin"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id, "type": "regular_user"}

@app.get("/calc/{a}/{op}/{b}")
def calculator(a: int, op: str, b: int):
    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    else:
        return {"error": "Operation not supported"}
        
    return {"a": a, "op": op, "b": b, "result": result}


@app.get("/status")
def get_time():
    new_dict ={
        "time": datetime,
        "hardcoded": "name_server"
    }
    return new_dict
    
    