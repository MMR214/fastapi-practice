from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
  return {'message': 'Hello World!'}


# @app.get('/blog/all')
# def get_all_blogs():
#   return {'message': 'All blogs provided'}
models.Base.metadata.create_all(engine)