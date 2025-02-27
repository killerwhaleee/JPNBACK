from fastapi import FastAPI
from routes.grammar import router as grammar_router
import sys

app = FastAPI()

# 注册 grammar 相关的路由
app.include_router(grammar_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


def home():
    return {"message": "Welcome to the Japanese Grammar API!"}


print(sys.getdefaultencoding())  # 检查默认编码
print(sys.stdout.encoding)  # 检查标准输出的编码
print(sys.stdin.encoding)  # 检查标准输入的编码
print(sys.getfilesystemencoding())  # 检查文件系统的编码
