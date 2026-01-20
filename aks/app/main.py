from fastapi import FastAPI, Header, HTTPException
import jwt, os

app = FastAPI()
SECRET = os.environ.get("JWT_SECRET", "supersecretkey")

@app.get("/secure-data")
def secure_data(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {
            "message": "Secure AKS response",
            "user": payload["sub"]
        }
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
