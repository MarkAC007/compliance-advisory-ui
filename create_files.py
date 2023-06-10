import os

directories = [
    "app/static/css",
    "app/static/js",
    "app/templates",
]

files = [
    "app/static/css/main.css",
    "app/static/js/main.js",
    "app/templates/base.html",
    "app/templates/index.html",
    "app/templates/references.html",
    "app/templates/iframes.html",
    "app/templates/console.html",
    "app/templates/scripts_menu.html",
    "app/app.py",
    "app/Dockerfile",
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

for file in files:
    open(file, "w").close()
