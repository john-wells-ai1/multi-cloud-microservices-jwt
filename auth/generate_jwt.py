import jwt, datetime

SECRET = "supersecretkey"

payload = {
    "sub": "user123",
    "iat": datetime.datetime.utcnow(),
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
}

token = jwt.encode(payload, SECRET, algorithm="HS256")
print(token)
