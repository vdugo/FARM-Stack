from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    delete_todo
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/')
async def root():
    return {"hello": "world"}

@app.get('/api/todo')
async def get_todos():
    return 1

@app.get('/api/todo/{id}')
async def get_todo_by_id():
    return 1

@app.post('/api/todo')
async def post_todo(todo):
    return 1

@app.put('/api/todo/{id}')
async def update_todo(id, data):
    return 1

@app.delete('/api/todo/{id}')
async def delete_todo(id):
    return 1