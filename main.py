from fastapi import FastAPI, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "123asd"
API_KEY_NAME = "Authorization"
api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def get_api_key(api_key_header = Security(api_key_header_auth)):
    if api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )

app = FastAPI()

@app.get("/")
def home():
    return {"data": "Minha API Python segura!"}

@app.get("protected", dependencies=[Security(get_api_key)])
def endpoint():
    return {"data": "Conteudo seguro!!!"}