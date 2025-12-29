import os
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey
from sqlalchemy import create_engine, text

app = FastAPI()

API_KEY = os.getenv("API_KEY")


api_key_header = APIKeyHeader(name="API-Key", auto_error=False)


def require_api_key(api_key: str = Security(api_key_header)):
    if not API_KEY or api_key != API_KEY:
        raise HTTPException(
            status_code=403, detail="Forbidden - Wrong API Key")


engine = create_engine(
    "sqlite:///./app.db",
    connect_args={"check_same_thread": False}
)


@app.get("/items")
def get_items(api_key: APIKey = Depends(require_api_key)):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM items"))
        return [dict(row) for row in result.mappings()]
