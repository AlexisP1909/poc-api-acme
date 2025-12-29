from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

engine = create_engine(
    "sqlite:///./app.db",
    connect_args={"check_same_thread": False}
)


@app.get("/items")
def get_items():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM items"))
        return [dict(row) for row in result.mappings()]
