from fastapi import FastAPI, HTTPException

app = FastAPI()

FAKE_DB = {
    "123": {"id": "123", "name": "Mark Wells", "role": "Engineer"}
}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id not in FAKE_DB:
        raise HTTPException(status_code=404, detail="User not found")
    return FAKE_DB[user_id]
