# Compliance Advisory Application

This application provides an intuitive user interface and navigation system for a compliance advisory business. It includes features such as updating references, displaying iframes, a console window for running Python scripts, and a menu of Python scripts.

## Prerequisites

- Python 3.8 or higher
- Flask 2.0.1 or higher
- Docker (optional)

## Project Structure

```
.
├── app.py
├── Dockerfile
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── main.js
└── templates
    ├── base.html
    ├── console.html
    ├── index.html
    ├── iframe.html
    └── references.html
```

## Setup

1. Clone the repository:

```
git clone https://github.com/yourusername/compliance-advisory.git
cd compliance-advisory
```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Running the Application

1. Run the application:

```
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Running the Application with Docker (optional)

1. Build the Docker image:

```
docker build -t compliance-advisory .
```

2. Run the Docker container:

```
docker run -d -p 5000:5000 --name compliance-advisory compliance-advisory
```

3. Open your web browser and navigate to `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
