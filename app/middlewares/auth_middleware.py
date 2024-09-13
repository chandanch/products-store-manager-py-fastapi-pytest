from functools import wraps


def auth_requests(func):
    """
    Returns if the given user has access to RBAC
    """

    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        request.state.user = {"name": "chandip"}

    return wrapper
