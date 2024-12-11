from fastapi import FastAPI
from helper import run_python_code, Request
from fastapi.responses import RedirectResponse
import uuid

app = FastAPI()

session_store = {}

@app.get("/")
def docs():
    return RedirectResponse(url="/docs")


@app.post("/execute")
async def execute(input: Request):
    if input.id is None:
        id = str(uuid.uuid4())
        session_store[id] = input.code
    else:
        id = input.id
        try:
            input.code = session_store[id] + "\n" + input.code
        except KeyError:
            return {"error": "Invalid ID"}

    response = run_python_code(input.code)
    response["id"] = id
    return response
