# Backend testing report

## Rest_API testing

###  1. Postman

Methods:

- Get Request:

     route: /

    returns:


    {
        "courses": [
            "frontend",
            "backend",
            "gamedev"
        ]
    }

Error: Incorrect courses data, absence of a "fullstack" course in list of courses 

_Solution: Add "fullstack" course to [backend/app.py] section app.get, 'data = {"courses":..'}_ 

- Post Request

  route: /login
  
  returns:


    {
      "message": "you've logged in"
    }

  if  fails returns:
  
    {
      null
    }

Error: The answer in case of failure does not correspond to the technical task:
    
    {
      "message": "username or password incorrect"
    }

_Solution: Add if condition to the main file [backend/app.py], section app.post(/login)_

- Get Request

  route:/registration

  returns:

      {
      "new user": {
          "username": "joe",
          "password": "12345678"
          "e-mail": "joe@doe.com"
      }
        }

if fails, returns: message with field missing specified.

    {
    "message": "Missing required fields: e-mail"
    }
Error: None

_Remark: This request works correctly, according to the technical task_

- Post Request 

  route://user//courses/add

  returns:

        {
    "message": "User joe courses saved successfully."
        }

if fails, returns: if course list empty:

    {
    "message": "No courses provided or the courses list is empty."
    }
if course isn't available:

    {
    "message": "The following courses are not available: math"
    }
if json error:

    {
    "message": "Error"
    }

Error: Incorrect error message (If json error)

_Solution: Correct the error  message in [backend/app.py], section @app.post("/user/{username}/courses/add")_

"message": "Invalid JSON payload."
