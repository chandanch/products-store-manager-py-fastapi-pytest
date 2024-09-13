from fastapi import Request
from functools import wraps


def auth_requests(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        # Simulate checking for 'auth' in request (modify as per your actual logic)
        if not request.headers.get("Authorization"):
            print("Auth Not found")
            raise Exception("Auth Not Found")

        # Set some user information in request state (if needed)
        request.state.user = {"name": "chandip"}

        # Call the actual function after auth
        return await func(*args, **kwargs)

    return wrapper
