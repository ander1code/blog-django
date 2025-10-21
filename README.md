# blogdjango

Prototype of a Blog developed using _Django_ and _SQLite_ database.

---

## 🚀 Features

- Uses _Bootstrap_ for responsive and elegant templates.
- Each post is linked to a previously registered user.
- Only the author of a post can edit or delete it.
- Includes user authentication: _Login_ and password protection.
- Certain actions are restricted to authenticated users.
- Comes with a built-in administrative interface (_Superuser_) for managing content and users.

---

## 🛠️ Software Stack

- **Python** 3.13.7  
- **Django** 5.2.7  
- **SQLite** 3  
- **Bootstrap** 3.3.7  

---

## 📁 Project Structure

blogdjango
|
│   .gitignore
│   manage.py
│   README.md
│
├───blog
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   ├───static
│   │   ├───css
│   │   │       bootstrap-theme.css
│   │   │       bootstrap-theme.css.map
│   │   │       bootstrap-theme.min.css
│   │   │       bootstrap-theme.min.css.map
│   │   │       bootstrap.css
│   │   │       bootstrap.css.map
│   │   │       bootstrap.min.css
│   │   │       bootstrap.min.css.map
│   │   │       style.css
│   │   │
│   │   ├───fonts
│   │   │       glyphicons-halflings-regular.eot
│   │   │       glyphicons-halflings-regular.svg
│   │   │       glyphicons-halflings-regular.ttf
│   │   │       glyphicons-halflings-regular.woff
│   │   │       glyphicons-halflings-regular.woff2
│   │   │
│   │   ├───image
│   │   │       favicon.png
│   │   │       
│   │   └───js
│   │           blog.js
│   │           bootstrap.js
│   │           bootstrap.min.js
│   │           jquery-3.2.1.min.js
│   │           npm.js
│   │
│   ├───templates
│   │   │   index.html
│   │   │
│   │   ├───home
│   │   │       home.html
│   │   │
│   │   ├───login
│   │   │       login.html
│   │   │
│   │   ├───post
│   │   │       form.html
│   │   │       show.html
│   │   │
│   │   └───_partials
│   │           errors.html
│   │           footer.html
│   │           header.html
│   │           message.html
│   │
│   ├───utils
│   │   │   utils.py
│   │   │
│   │   └───__pycache__
│   └───__pycache__
├───blogdjango
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
└───media
    └───posts
            noimage.png