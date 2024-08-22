from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import uvicorn  # FastAPI uses uvicorn as the ASGI server

app = FastAPI()

@app.get('/')
def home():
    return JSONResponse(content={"message": "This is service 1"})

@app.get('/foo')
def foo():
    response = requests.get('http://localhost:5001/')
    return JSONResponse(content={"message": "Received response from service 2", "data": response.json()})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
