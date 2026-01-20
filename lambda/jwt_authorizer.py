import jwt, os

SECRET = os.environ.get("JWT_SECRET", "supersecretkey")

def lambda_handler(event, context):
    token = event["authorizationToken"].replace("Bearer ", "")
    try:
        jwt.decode(token, SECRET, algorithms=["HS256"])
        return allow(event["methodArn"])
    except jwt.InvalidTokenError:
        return deny(event["methodArn"])

def allow(arn):
    return policy("user", "Allow", arn)

def deny(arn):
    return policy("user", "Deny", arn)

def policy(principal, effect, arn):
    return {
        "principalId": principal,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "execute-api:Invoke",
                "Effect": effect,
                "Resource": arn
            }]
        }
    }
