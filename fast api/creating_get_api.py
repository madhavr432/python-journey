from fastapi import FastAPI
app = FastAPI(
    title = "Hackathon API",
    description = "Live demo API for the hackathon project",
    version = "1.0.0"
)
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Backend!", "status":"online"}
@app.get("/handler")
def handler():
    return{ "data": "from handler"}