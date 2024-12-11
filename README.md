# PyServer Application Guide

1. Create and activate virtual environment (optional but recommended):
```bash
python -m venv venv
```

for mac/linux

```
source venv/bin/activate
```

for windows

```
.\venv\Scripts\activate.bat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The server will start at `http://localhost:8000`

2. Access the API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Running Tests
Execute tests using pytest:
```bash
pytest
```
## Docker Build Guide
1. Build the Docker image:
```bash
docker build -t pyserver .
```

2. Run the Docker container:
```bash
docker run -p 8000:8000 pyserver
```

The application will be accessible at `http://localhost:8000`
