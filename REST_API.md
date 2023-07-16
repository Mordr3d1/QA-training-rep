# REST API docs

This is small API for testing. This API works for e-courses site. <br>

route: / <br>
description: route used to retrieve info about courses available.
method: GET <br>
returns:
<pre>
{
    "courses": [
        "frontend",
        "backend",
        "fullstack",
        "gamedev"
    ]
}
</pre>
<br>
route: /login <br>
description: <br>
gets: <br>
method: POST <br>
returns:
<pre>
{
    "message": "you've logged in"
}
</pre>
if fails, returns:
<pre>
{
    "message": "username or password incorrect"
}
</pre>
<br>
route: /registration <br>
description: this route should get username, password and e-mail for registration.
gets: [username, password, e-mail]
method: POST <br>
returns:
<pre>
{
    "new user": {
        "username": "joe",
        "password": "12345678"
        "e-mail": "joe@doe.com"
    }
}
</pre>
if fails, returns: message with field missing specified.
<pre>
{
    "message": "Missing required fields: e-mail"
}
</pre>
<br>
route: /user/<username>/courses/add <br>
description: function used to add courses to user by username <br>
gets: <br>
returns:
<pre>
{
    "message": "User joe courses saved successfully."
}
</pre>
if fails, returns:
if course list empty:
<pre>
{
    "message": "No courses provided or the courses list is empty."
}
</pre>
if course isn't available:
<pre>
{
    "message": "The following courses are not available: math"
}
</pre>
if json error:
<pre>
{
    "message": "Invalid JSON payload."
}
</pre>
