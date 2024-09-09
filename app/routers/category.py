from fastapi import APIRouter

category_router = APIRouter()


@category_router.post("/")
def add_category():
    return {"status": "Added"}
