
# API Gateway Configuration

## Steps
1. Create REST API
2. Add `/proxy` resource
3. Enable Lambda Proxy Integration
4. Attach Lambda Authorizer (jwt_authorizer.py)
5. Require Authorization header
6. Deploy API

## Authorization
- Type: Lambda Authorizer
- Token Source: Authorization
- TTL: 300 seconds
