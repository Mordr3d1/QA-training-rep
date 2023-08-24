from fastapi import FastAPI, Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.get("/")
async def index():
    data = {"courses": ["frontend", "backend", "gamedev", "fullstack"]}
    return data

@app.post("/login")
async def login(request: Request):
    user = {
        "username":"joe",
        "password":"12345678"
        }
    user_logging = await request.json()
    if user == user_logging:
        return {"message":"you've logged in"}
    else:
        return {"message": "username or password incorrect"}

@app.get("/registration")
async def reg(request: Request):
    new_user = await request.json()
    required_fields = ["username", "password"]

    missing_fields = [field for field in required_fields if field not in new_user]
    if missing_fields:
        return {"message": f"Missing required fields: {', '.join(missing_fields)}"}

    return {"new user": new_user}

@app.post("/user/{username}/courses/add")
async def save_user_courses(username: str, request: Request):
    available_courses = ["frontend", "backend", "gamedev"]
    try:
        data = await request.json()
        courses = data.get("courses", [])

        if not courses:
            return {"message": "No courses provided or the courses list is empty."}

        if not isinstance(courses, list):
            return {"message": "Courses should be provided as a list."}

        unavailable_courses = [course for course in courses if course not in available_courses]
        if unavailable_courses:
            return {"message": f"The following courses are not available: {', '.join(unavailable_courses)}"}

        return {"message": f"User {username} courses saved successfully."}

    except ValueError:
        return {"message": "Invalid JSON payload."}


