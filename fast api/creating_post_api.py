from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI app!"}


@app.post("/greet")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
