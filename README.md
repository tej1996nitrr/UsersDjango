# UsersDjango

A Django Rest Framework application build for content sharing. 

## Features:
1. Store , share and view the content (images, urls, links, bookmarks, articles etc.)
2. User Registration.
3. Token Based user authentication.
4. Create User profile (profile picture, bio, city etc.)
5. View other users' profile and their posts.
6. Object level permissions
7.Classification of each post based on categories.

# Requirements:
1. django = "3.0"
2. djangorestframework = "3.11.0"
3. django-allauth = "*"
4. django-rest-auth = "*"
5. coreapi = "==2.3.3"
6. pyyaml = "==5.1.2"
7. coverage = "5.0.4"
python_version = "3.7"


# API Documentation:
Docs at: http://127.0.0.1:8000/docs/
1. Registration: http://127.0.0.1:8000/api/rest-auth/registration/
2. Login:  http://127.0.0.1:8000/api/rest-auth/login/
3. Logout:  http://127.0.0.1:8000/api/rest-auth/logout/
4. To view all posts: GET http://127.0.0.1:8000/posts/
5. Create a post(for logged in users) POST http://127.0.0.1:8000/posts/
6. Read a particular post GET http://127.0.0.1:8000/posts/{id}
7. Update a post(only for author of the post) PUT http://127.0.0.1:8000/posts/{id}
8. Delete a post(only for author of the post) DELETE http://127.0.0.1:8000/posts/{id}
9. View all profiles :/users/profiles/
10.  View all posts/details of a particular user /users/profiles/{id}/
11. Update profile(for owner only)  UPDATE http://127.0.0.1:8000//users/profiles/{id}/
12. Delete profile DELETE http://127.0.0.1:8000//users/profiles/{id}/

# Screenshots:
https://github.com/tej1996nitrr/UsersDjango/tree/UsersBranch/Screenshots

# Test Coverage:

(requirement= coverage = "5.0.4")
To run coverage using local terminal:
1. pipenv install coverage==5.0.4
2. coverage run  manage.py test
3. coverage report

https://github.com/tej1996nitrr/UsersDjango/blob/UsersBranch/Test%20Coverage.png

# Project branches:
1. Master-> contains basic Posts app
2. UsersBranch-> contains all the functionalities including registration and custom users
3. UsersToken-> Implementation of Login, Logout, Registration without 3rd party packages

# Run the project Locally:
1. Clone the "UsersBranch" branch of this repo.
2. Install the pipenv requirements
3. Go to directory of manage.py -> Run migrations:python manage.py migrate
4. To run the server.-> python manage.py runserver
