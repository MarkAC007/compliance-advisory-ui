import os

# Create directories
dirs = [
    "app",
    "app/modules",
    "app/templates",
    "app/static",
    "app/static/css",
    "app/static/js",
    "app/static/images",
    "tests",
]

for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

# Create files
files = {
    "app/__init__.py": "",
    "app/main.py": "",
    "app/modules/__init__.py": "",
    "app/templates/base.html": "",
    "app/static/css/main.css": "",
    "app/static/js/main.js": "",
    "tests/__init__.py": "",
    "tests/test_app.py": "",
    "Dockerfile": "",
    ".dockerignore": "",
    "requirements.txt": "",
    "README.md": "",
}

for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Project structure created successfully.")